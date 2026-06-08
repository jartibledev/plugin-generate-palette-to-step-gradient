# [:uk:](README_EN.md) [:de:](README_DE.md) [:es:](README_ES.md)  
# Palette to Step Gradient Generator - GIMP 3.0 Plugin

**Palette to Step Gradient Generator** est un plugin développé en Python pour **GIMP 3.0**, conçu spécifiquement pour les **artistes de Pixel Art**. Il automatise le processus fastidieux de création de palettes d'ombrage et de dégradés.

Grâce à une interface utilisateur interactive, il vous suffit de choisir une couleur de base et le nombre d'étapes. Le plugin calcule automatiquement une palette monochromatique basée sur le système TSL (HSV) et la luminance, l'enregistre dans GIMP et génère instantanément un **dégradé par étapes (Step Gradient)** avec des contours nets (sans transition fluide), prêt à être utilisé avec vos outils de dessin.

## ✨ Fonctionnalités

* **Interface graphique interactive :** Une boîte de dialogue facile à utiliser avec un sélecteur de couleurs GTK natif, un compteur d'étapes et un champ de saisie pour le nom.
* **Palettes monochromatiques intelligentes :** Calcule automatiquement des rampes de couleurs (claires/sombres) harmonieuses à partir d'une seule couleur de base grâce à la manipulation TSL.
* **Enregistrement instantané dans GIMP :** Sauvegarde les couleurs générées sous la forme d'une palette standard de GIMP.
* **Dégradés prêts pour le Pixel Art :** Convertit automatiquement la nouvelle palette en un dégradé GIMP, en divisant les segments de manière uniforme et en configurant la fonction de mélange sur `STEP` (idéal pour l'ombrage net en couleurs indexées propre au pixel art).

---

## 🛠️ Configuration requise

* **GIMP 3.0** (ou version supérieure) avec prise en charge des plugins Python 3.
* GTK 3.0 et l'introspection d'objets GNOME (`PyGObject`, `Gio`, `Gegl`, `Gimp 3.0`).

---

## 🔧 Installation

1. **Téléchargez** le fichier du script et nommez-le `py3-generate-palette-to-step-gradient.py`.
2. **Rendez le fichier exécutable :**
   * *Sur Linux/macOS :* Ouvrez un terminal et exécutez `chmod +x py3-generate-palette-to-step-gradient.py`.
3. **Déplacez le fichier** dans votre répertoire de plug-ins GIMP 3.0 :
   * **Linux :** `~/.config/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`
   * **Windows :** `%APPDATA%\GIMP\3.0\plug-ins\py3-generate-palette-to-step-gradient\`
   * **macOS :** `~/Library/Application Support/GIMP/3.0/plug-ins/py3-generate-palette-to-step-gradient/`

> 💡 **Note :** GIMP 3.0 exige que les plugins soient placés dans un dossier portant exactement le même nom que le script (sans l'extension `.py`).

4. Redémarrez GIMP.

---

## 📖 Mode d'emploi

1. Ouvrez GIMP et allez dans le menu supérieur : **`<Image>` > `Palette to Gradient`**.
2. Une boîte de dialogue apparaît :
   * **Color :** Cliquez sur le bouton de couleur pour choisir votre ton moyen de base.
   * **SpinButton :** Sélectionnez le nombre de couleurs/étapes que doit comporter votre rampe d'ombrage.
   * **Entry :** Saisissez un nom pour votre nouvelle palette et votre dégradé.
3. Cliquez sur **Create Palette**.
4. Vérifiez vos onglets **Palettes** et **Dégradés** dans GIMP ; votre nouveau dégradé par étapes est sélectionné et prêt à l'emploi !

---

## ✍️ Auteur
* **Développé par :** Sergio Maya López
* **Année :** 2026
