# [:uk:](README.md) [:es:](README_ES.md) [:fr:](README_FR.md) 
# Palette to Step Gradient Generator - GIMP 3.0 Plugin

**Palette to Step Gradient Generator** ist ein in Python entwickeltes Plugin für **GIMP 3.0**, das speziell für **Pixel-Art-Künstler** entworfen wurde. Es automatisiert den mühsamen Prozess der Erstellung von Schattierungspaletten und Farbverläufen.

Über eine interaktive Benutzeroberfläche wählen Sie einfach eine Basisfarbe und die Anzahl der Schritte. Das Plugin berechnet automatisch eine monochromatische Palette auf Basis von HSV und Luminanz, registriert diese in GIMP und erstellt sofort einen **abgestuften Farbverlauf (Step Gradient)** mit harten Kanten (ohne weiche Übergänge), der direkt mit Ihren Malwerkzeugen verwendet werden kann.

## ✨ Funktionen

* **Interaktive GUI:** Leicht bedienbarer Dialog mit nativem GTK-Farbauswähler, Schrittzähler und Namenseingabefeld.
* **Intelligente monochromatische Paletten:** Berechnet durch HSV-Manipulation automatisch visuell ansprechende Hell-Dunkel-Farbrampen aus einer einzigen Basisfarbe.
* **Sofortige GIMP-Registrierung:** Speichert die generierten Farben als Standard-GIMP-Palette.
* **Pixel-Art-bereite Farbverläufe:** Konvertiert die neue Palette automatisch in einen GIMP-Farbverlauf, teilt die Segmente gleichmäßig auf und setzt die Mischfunktion auf `STEP` (perfekt für scharfe Schattierungen im Pixel-Art-Stil mit indizierten Farben).

---

## 🛠️ Anforderungen

* **GIMP 3.0** (oder höher) mit Unterstützung für Python 3-Plugins.
* GTK 3.0 und GNOME Object Introspection (`PyGObject`, `Gio`, `Gegl`, `Gimp 3.0`).

---

## 🔧 Installation

1. **Laden Sie die Skriptdatei herunter** und benennen Sie sie in `py3-generate-palette-to-step-gradient.py` um.
2. **Machen Sie die Datei ausführbar:**
   * *Unter Linux/macOS:* Öffnen Sie ein Terminal und führen Sie `chmod +x py3-generate-palette-to-step-gradient.py` aus.
3. **Verschieben Sie die Datei** in Ihr GIMP 3.0 Plug-ins-Verzeichnis:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\py3-generate-palette-to-step-gradient\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`

> 💡 **Hinweis:** GIMP 3.0 erfordert, dass sich Plugins in einem Ordner befinden, der exakt denselben Namen wie das Skript trägt (ohne die Dateiendung `.py`).

4. Starten Sie GIMP neu.

---

## 📖 Bedienung

1. Öffnen Sie GIMP und gehen Sie im oberen Menü auf: **`<Image>` > `Palette to Gradient`**.
2. Ein Dialogfenster wird geöffnet:
   * **Color:** Klicken Sie auf die Farbschaltfläche, um Ihren Basis-Mittelton zu wählen.
   * **SpinButton:** Wählen Sie aus, wie viele Farben/Schritte Ihre Schattierungsrampe haben soll.
   * **Entry:** Geben Sie einen Namen für Ihre neue Palette und Ihren Farbverlauf ein.
3. Klicken Sie auf **Create Palette**.
4. Überprüfen Sie Ihre **Paletten-** und **Farbverlauf-Docks** in GIMP; Ihr neuer abgestufter Farbverlauf ist bereits ausgewählt und einsatzbereit!

---

## ✍️ Autor
* **Entwickelt von:** Sergio Maya López
* **Jahr:** 2026
