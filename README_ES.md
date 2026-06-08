# [:uk:](README_EN.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
# Palette to Step Gradient Generator - GIMP 3.0 Plugin

**Palette to Step Gradient Generator** es un plugin desarrollado en Python para **GIMP 3.0**, diseñado específicamente para **artistas de Pixel Art**. Automatiza el tedioso proceso de crear paletas de sombreado y degradados.

A través de una interfaz de usuario interactiva, solo necesitas elegir un color base y el número de pasos. El plugin calcula automáticamente una paleta monocromática basada en HSV y luminancia, la registra en GIMP y genera instantáneamente un **Degradado por pasos (Step Gradient)** con bordes duros (sin transiciones suaves), listo para ser usado con tus herramientas de pintura.

## ✨ Características

* **Interfaz gráfica interactiva:** Un diálogo fácil de usar con un selector de color nativo de GTK, un contador de pasos y un campo para introducir el nombre.
* **Paletas monocromáticas inteligentes:** Calcula automáticamente rampas de color (claras y oscuras) armoniosas a partir de un solo color base mediante la manipulación de valores HSV.
* **Registro instantáneo en GIMP:** Guarda los colores generados directamente como una paleta estándar de GIMP.
* **Degradados listos para Pixel Art:** Convierte automáticamente la nueva paleta en un degradado de GIMP, dividiendo los segmentos de manera uniforme y configurando la función de mezcla en modo `STEP` (perfecto para el sombreado definido con colores indexados propio del pixel art).

---

## 🛠️ Requisitos

* **GIMP 3.0** (o superior) con soporte para plugins de Python 3.
* GTK 3.0 e introspección de objetos GNOME (`PyGObject`, `Gio`, `Gegl`, `Gimp 3.0`).

---

## 🔧 Instalación

1. **Descarga** el archivo del script y nómbralo `py3-generate-palette-to-step-gradient.py`.
2. **Dale permisos de ejecución al archivo:**
   * *En Linux/macOS:* Abre una terminal y ejecuta `chmod +x py3-generate-palette-to-step-gradient.py`.
3. **Mueve el archivo** a tu directorio de plugins de GIMP 3.0:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\py3-generate-palette-to-step-gradient\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`

> 💡 **Nota:** GIMP 3.0 requiere que los plugins estén dentro de una carpeta que tenga exactamente el mismo nombre que el archivo del script (sin la extensión `.py`).

4. Reinicia GIMP.

---

## 📖 Modo de Uso

1. Abre GIMP y ve al menú superior: **`<Image>` > `Palette to Gradient`**.
2. Aparecerá una ventana de diálogo:
   * **Color:** Haz clic en el botón de color para elegir tu tono medio base.
   * **SpinButton:** Selecciona cuántos colores/pasos quieres que tenga tu rampa de sombreado.
   * **Entry:** Escribe un nombre para tu nueva paleta y degradado.
3. Haz clic en **Create Palette**.
4. ¡Listo! Revisa tus paneles de **Paletas** y **Degradados** en GIMP; tu nuevo degradado por pasos ya estará seleccionado y preparado para pintar.

---

## ✍️ Autor
* **Desarrollado por:** Sergio Maya López
* **Año:** 2026
