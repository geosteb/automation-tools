import os
import shutil
import PyPDF2

# --- CONFIGURACIÓN DE RUTAS ---
# Esta es la carpeta donde tienes los 1800 PDFs
RUTA_ORIGEN = r'C:\Users\geost\Documents\0 - WIKINGENIERIA\Web\Cursor\geosteb_uhu_pdfs_vault'
# Carpeta donde moveremos los archivos administrativos/basura
CARPETA_DESCARTE = os.path.join(RUTA_ORIGEN, 'DESCARTE_ADMINISTRATIVO')

# --- CRITERIOS DE FILTRADO ---
# Si el PDF contiene alguna de estas palabras, se moverá a DESCARTE
KEYWORDS_BASURA = [
    'factura', 'recibo', 'pago', 'tasas', 'matricula', 'convocatoria', 
    'listado', 'asistencia', 'justificante', 'dni', 'expediente', 
    'automatricula', 'ordinaria', 'extraordinaria', 'papeleta'
]

# Si el PDF contiene esto, NO se mueve (protección extra)
KEYWORDS_PROTECCION = ['∑', '∫', 'Δ', 'π', '∞', 'ohm', 'vatios', 'hertz']

if not os.path.exists(CARPETA_DESCARTE):
    os.makedirs(CARPETA_DESCARTE)

print(f"--- Iniciando triaje en: {RUTA_ORIGEN} ---")

archivos = [f for f in os.listdir(RUTA_ORIGEN) if f.lower().endswith('.pdf')]
contador_descartados = 0

for archivo in archivos:
    ruta_pdf = os.path.join(RUTA_ORIGEN, archivo)
    moverse_a_descarte = False
    
    try:
        with open(ruta_pdf, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            # Analizamos las 3 primeras páginas para estar seguros
            texto_completo = ""
            for i in range(min(3, len(reader.pages))):
                texto_completo += reader.pages[i].extract_text().lower()
            
            # 1. Comprobamos si tiene palabras de basura
            if any(word in texto_completo for word in KEYWORDS_BASURA):
                moverse_a_descarte = True
            
            # 2. Protección: Si tiene símbolos de ingeniería, lo salvamos del descarte
            if any(sym in texto_completo for sym in KEYWORDS_PROTECCION):
                moverse_a_descarte = False

    except Exception as e:
        print(f"No se pudo leer {archivo}: {e} (Se queda en origen por seguridad)")
        continue

    # Acción de mover
    if moverse_a_descarte:
        try:
            shutil.move(ruta_pdf, os.path.join(CARPETA_DESCARTE, archivo))
            contador_descartados += 1
            print(f"[DESCARTADO] -> {archivo}")
        except Exception as e:
            print(f"Error al mover {archivo}: {e}")

print(f"\n--- TRABAJO FINALIZADO ---")
print(f"Archivos analizados: {len(archivos)}")
print(f"Archivos movidos a descarte: {contador_descartados}")
print(f"Los archivos valiosos permanecen en la carpeta raíz.")