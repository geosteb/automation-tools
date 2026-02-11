# Automation Tools 🛠️

A collection of lightweight and efficient scripts designed to optimize different type of tasks that will save you time.

---

## 🐍 Python Utilities

### 1. Photo Sorter (HSV Analysis)
Automated tool to distinguish and separate **Black & White** images from **Color** photos within large datasets.

* **Logic:** The algorithm converts pixel data into the **HSV** color space and calculates the average saturation.
* **Decision Engine:** If the average saturation falls below the calibrated threshold (`sat < 0.250`), the image is classified as B&W and moved to the destination folder.
* **Stack:** Python 3.x, Pillow (PIL), Colorsys.

### 2. Recursive PDF Copier
A file mining utility that locates and centralizes PDF documents hidden within complex subfolder structures.

* **Recursive Scan:** Performs a deep search through all nested directories.
* **Collision Safety:** Features an **intelligent renaming system**. If files share the same name across different paths, it appends a numeric suffix to prevent data loss or overwrites.
* **Stack:** Python 3.x, Shutil, OS.

---

## 🚀 Quick Start

1. **Configuration (PDF Copier):** Open the script and update the `ORIGEN` / `DESTINO` (or `CARPETA`) paths.
2. **Calibration (Photo Sorter):** Adjust the `0.250` value to fine-tune sensitivity for muted colors or sepia tones.
3. **Execution:** Use the following command in your terminal:
```bash
python script_name.py
```

---

## 👨‍💻 Author
**Designed by Geosteb, enhanced by AI collaboration**

---
