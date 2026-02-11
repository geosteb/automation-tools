import os
from PIL import Image
import colorsys

CARPETA = r"ruta"
DESTINO = r"ruta_destino"

os.makedirs(DESTINO, exist_ok=True)

def saturacion_media(img):
    img = img.convert("RGB")
    w, h = img.size
    pixels = img.load()

    total_s = 0
    count = 0

    step_x = max(1, w // 40)
    step_y = max(1, h // 40)

    for x in range(0, w, step_x):
        for y in range(0, h, step_y):
            r, g, b = pixels[x, y]
            h_, s_, v_ = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            total_s += s_
            count += 1

    return total_s / count

for archivo in os.listdir(CARPETA):
    if not archivo.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    ruta = os.path.join(CARPETA, archivo)
    try:
        img = Image.open(ruta)
        sat = saturacion_media(img)

        if sat < 0.250:   # Umbral ajustado para fotos b/n reales
            os.rename(ruta, os.path.join(DESTINO, archivo))
            print(f"BN → {archivo} (sat={sat:.3f})")
        else:
            print(f"COLOR → {archivo} (sat={sat:.3f})")

    except Exception as e:
        print(f"Error con {archivo}: {e}")

