# [:es:](README_ES.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
# Palette to Step Gradient Generator - GIMP 3.0 Plugin

**Palette to Step Gradient Generator** is a Python-based plugin for **GIMP 3.0** designed specifically for **Pixel Artists**. It automates the tedious process of creating shading palettes and gradients.

With an interactive UI, you simply choose a base color and the number of steps. The plugin automatically calculates a monochromatic palette based on HSV and luminance, registers it in GIMP, and instantly generates a **Step Gradient** (hard edges, no smooth blending) ready to be used with your painting tools.

## ✨ Features

* **Interactive GUI:** Easy-to-use dialog with a native GTK color picker, step counter, and name input.
* **Smart Monochromatic Palettes:** Automatically calculates visually appealing light/dark ramps from a single base color using HSV manipulation.
* **Instant GIMP Registration:** Saves the generated colors as a standard GIMP Palette.
* **Pixel Art Ready Gradients:** Automatically converts the new palette into a GIMP Gradient, splitting the segments uniformly and setting the blending function to `STEP` (perfect for sharp, indexed-color pixel art shading).

---

## 🛠️ Requirements

* **GIMP 3.0** (or higher) with Python 3 Plugin support.
* GTK 3.0 and GNOME Object Introspection (`PyGObject`, `Gio`, `Gegl`, `Gimp 3.0`).

---

## 🔧 Installation

1. **Download** the script file and name it `py3-generate-palette-to-step-gradient.py`.
2. **Make the file executable:**
   * *Linux/macOS:* Open a terminal and run `chmod +x py3-generate-palette-to-step-gradient.py`.
3. **Move the file** to your GIMP 3.0 plug-ins directory:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\py3-generate-palette-to-step-gradient\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`

> 💡 **Note:** GIMP 3.0 requires plugins to be inside a folder with the exact same name as the script (without the `.py` extension).

4. Restart GIMP.

---

## 📖 How to Use

1. Open GIMP and go to the top menu: **`<Image>` > `Palette to Gradient`**.
2. A dialog will appear:
   * **Color:** Click the color button to choose your base mid-tone.
   * **SpinButton:** Select how many colors/steps your shading ramp should have.
   * **Entry:** Type a name for your new palette and gradient.
3. Click **Create Palette**.
4. Check your **Palettes** and **Gradients** docks in GIMP; your new step gradient is selected and ready to use!

---

## ✍️ Author
* **Developed by:** Sergio Maya López
* **Year:** 2026
