# 🇨🇱 Burp RUT Generator Extension

![Burp Suite](https://img.shields.io/badge/Burp%20Suite-Extension-orange?logo=burp-suite&style=flat-square)
![Python](https://img.shields.io/badge/Built%20with-Jython-blue?logo=python&style=flat-square)
![Made in Chile](https://img.shields.io/badge/Made%20in-Chile-red?style=flat-square)

Una extensión para Burp Suite que permite generar **RUTs chilenos aleatorios** directamente desde la interfaz de Burp. Útil para pruebas de QA, validaciones de formularios o pentesting en aplicaciones que requieren ingreso de RUTs válidos.

---

## ✨ Funcionalidades

✅ Generación masiva de RUTs aleatorios  
✅ Interfaz integrada como pestaña en Burp Suite  
✅ Opciones de formato:
- 🔹 Sin puntos ni guión
- 🔹 Sin dígito verificador (DV)
- 🔹 Solo guión sin puntos  
✅ Botón para copiar todos los RUTs al portapapeles  
✅ Interfaz visualmente mejorada con fuentes más grandes y claras

---

## 🖼️ Captura de Pantalla

![screenshot](https://i.imgur.com/S5Ma5yJ.png)

---

## 🛠️ Requisitos

- [Burp Suite](https://portswigger.net/burp)
- [Jython standalone 2.7.x](https://www.jython.org/download)

---

## ⚙️ Instalación

1. Abre Burp Suite
2. Ve a la pestaña `Extensions`
3. Dar al botón "add"
4. Añade el archivo `.py` como una nueva extensión escrita en Python (Jython)
5. Asegúrate de tener el Jython .jar cargado en la sección `Options > Python Environment`

---

## 📋 Uso

1. Dirígete a la pestaña **"RUT Generator"**
2. Ingresa la cantidad de RUTs que deseas generar
3. Marca las opciones de formato deseadas
4. Haz clic en "Generar RUTs"
5. Copia al portapapeles con un solo clic

---

## 🧠 Sobre el RUT

El Rol Único Tributario (RUT) es un identificador único usado en Chile, similar a un número de identificación fiscal. Esta extensión utiliza el algoritmo de módulo 11 para calcular el dígito verificador.

---

## ✍️ Autor

**by 1_4tom0**


## ⚠️ Disclaimer

Esta herramienta fue desarrollada únicamente con fines educativos y éticos.  
**No me hago responsable por el mal uso que se le pueda dar.**  
**Úsala siempre con consentimiento y en entornos controlados.**
