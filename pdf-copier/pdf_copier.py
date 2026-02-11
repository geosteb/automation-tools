import os
import shutil

# --- CONFIGURACIÓN ---
CARPETA_ORIGEN = r"G:\[ studies ]\Universidad"   # Cambia esto por tu ruta origen
CARPETA_DESTINO = r"C:\Users\geost\Documents\0 - WIKINGENIERIA\Web\Cursor\wikingenieria-web\assets\data\geosteb_uhu_pdfs" # Cambia esto por tu ruta destino

def buscar_y_copiar_pdfs(origen, destino):
    # Crear carpeta destino si no existe
    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"✅ Carpeta creada: {destino}")

    contador = 0
    errores = 0

    print(f"🔎 Buscando PDFs en: {origen}...")
    print("-" * 50)

    # Recorrer todo el árbol de directorios (recursivo)
    for root, dirs, files in os.walk(origen):
        for file in files:
            if file.lower().endswith('.pdf'):
                ruta_completa_origen = os.path.join(root, file)
                ruta_completa_destino = os.path.join(destino, file)

                # Evitar sobreescribir si ya existe un archivo con el mismo nombre
                nombre_base, extension = os.path.splitext(file)
                copia_n = 1
                while os.path.exists(ruta_completa_destino):
                    nuevo_nombre = f"{nombre_base}_{copia_n}{extension}"
                    ruta_completa_destino = os.path.join(destino, nuevo_nombre)
                    copia_n += 1

                try:
                    shutil.copy2(ruta_completa_origen, ruta_completa_destino)
                    print(f"📄 Copiado: {file} -> {os.path.basename(ruta_completa_destino)}")
                    contador += 1
                except Exception as e:
                    print(f"❌ Error copiando {file}: {e}")
                    errores += 1

    print("-" * 50)
    print(f"🚀 PROCESO FINALIZADO.")
    print(f"Total PDFs copiados: {contador}")
    if errores > 0:
        print(f"Errores encontrados: {errores}")

if __name__ == "__main__":
    buscar_y_copiar_pdfs(CARPETA_ORIGEN, CARPETA_DESTINO)