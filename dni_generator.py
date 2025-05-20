# -*- coding: utf-8 -*-
from burp import IBurpExtender, ITab
from javax.swing import (
    JPanel, JLabel, JTextField, JButton, JScrollPane,
    JTextArea, BoxLayout, JCheckBox, BorderFactory
)
from java.awt import Color, Dimension, Font, Toolkit
from java.awt.datatransfer import StringSelection
import random

class BurpExtender(IBurpExtender, ITab):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("RUT/DNI Generator")

        self._panel = JPanel()
        self._panel.setLayout(BoxLayout(self._panel, BoxLayout.Y_AXIS))
        self._panel.setBackground(Color(245, 245, 250))  # Fondo suave

        # Fuente atractiva y grande
        fuente_general = Font("Segoe UI", Font.PLAIN, 14)
        fuente_textarea = Font("Courier New", Font.PLAIN, 13)

        label = JLabel("Cantidad de RUTs a generar:")
        label.setFont(fuente_general)
        self._panel.add(label)

        self.inputField = JTextField(5)
        self.inputField.setMaximumSize(Dimension(100, 30))
        self.inputField.setFont(fuente_general)
        self._panel.add(self.inputField)

        self._panel.add(JLabel(" "))

        self.cleanCheckBox = JCheckBox("Sin puntos ni guion")
        self.cleanCheckBox.setFont(fuente_general)
        self.cleanCheckBox.setBackground(Color(245, 245, 250))
        self._panel.add(self.cleanCheckBox)

        self.noDvCheckBox = JCheckBox("Sin dígito verificador")
        self.noDvCheckBox.setFont(fuente_general)
        self.noDvCheckBox.setBackground(Color(245, 245, 250))
        self._panel.add(self.noDvCheckBox)

        self.onlyDashCheckBox = JCheckBox("Solo guion (sin puntos)")
        self.onlyDashCheckBox.setFont(fuente_general)
        self.onlyDashCheckBox.setBackground(Color(245, 245, 250))
        self._panel.add(self.onlyDashCheckBox)

        self._panel.add(JLabel(" "))

        self.generateButton = JButton("Generar RUTs", actionPerformed=self.generar_ruts)
        self.generateButton.setFont(fuente_general)
        self.generateButton.setBackground(Color(220, 235, 255))
        self._panel.add(self.generateButton)

        self.copyButton = JButton("Copiar al portapapeles", actionPerformed=self.copiar_resultados)
        self.copyButton.setFont(fuente_general)
        self.copyButton.setBackground(Color(210, 245, 210))
        self._panel.add(self.copyButton)

        self._panel.add(JLabel(" "))

        label_resultados = JLabel("Resultados:")
        label_resultados.setFont(fuente_general)
        self._panel.add(label_resultados)
        
        self.resultArea = JTextArea(15, 40)
        self.resultArea.setFont(fuente_textarea)
        self.resultArea.setEditable(False)
        self.resultArea.setBackground(Color(255, 255, 245))
        self.resultArea.setBorder(BorderFactory.createLineBorder(Color.GRAY))
        scrollPane = JScrollPane(self.resultArea)
        self._panel.add(scrollPane)

        callbacks.addSuiteTab(self)

    def getTabCaption(self):
        return "RUT Generator"

    def getUiComponent(self):
        return self._panel

    def generar_ruts(self, event):
        try:
            cantidad = int(self.inputField.getText())
            sin_puntos_guion = self.cleanCheckBox.isSelected()
            sin_dv = self.noDvCheckBox.isSelected()
            solo_guion = self.onlyDashCheckBox.isSelected()
            resultados = []

            for _ in range(cantidad):
                rut = random.randint(1000000, 25000000)
                dv = self.calcular_dv(rut)
                rut_formateado = self.formatear_rut(rut, dv)

                if sin_puntos_guion:
                    rut_formateado = rut_formateado.replace(".", "").replace("-", "")
                elif solo_guion:
                    rut_formateado = rut_formateado.replace(".", "")  # deja el guion

                if sin_dv:
                    rut_formateado = rut_formateado.rsplit("-", 1)[0]  # elimina DV

                resultados.append(rut_formateado)

            self.resultArea.setText("\n".join(resultados))

        except Exception as e:
            self.resultArea.setText("Error: " + str(e))

    def copiar_resultados(self, event):
        texto = self.resultArea.getText()
        if texto.strip():
            clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
            selection = StringSelection(texto)
            clipboard.setContents(selection, None)
            self._callbacks.printOutput("Texto copiado al portapapeles.")
        else:
            self._callbacks.printOutput("No hay texto para copiar.")

    def calcular_dv(self, rut):
        factores = [2, 3, 4, 5, 6, 7]
        suma = 0
        rut_str = str(rut)
        for i in range(len(rut_str)-1, -1, -1):
            suma += int(rut_str[i]) * factores[(len(rut_str)-1 - i) % len(factores)]
        resto = 11 - (suma % 11)
        if resto == 11:
            return "0"
        elif resto == 10:
            return "K"
        else:
            return str(resto)

    def formatear_rut(self, rut, dv):
        rut_str = "{:,}".format(rut).replace(",", ".")
        return "{}-{}".format(rut_str, dv)
