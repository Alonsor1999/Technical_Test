
import os
import sys
from docx import Document
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def CreateFile():
    # Crear un nuevo documento de Word
    doc = Document()

    # Definir la ruta del archivo
    doc_path = os.path.expanduser("~/Documents/File.docx")

    # Verificar si el archivo ya existe
    if not os.path.exists(doc_path):
        # Guardar el documento solo si el archivo no existe
        doc.save(doc_path)
        print("Archivo de Word creado con éxito en:", doc_path)
    else:
        print("El archivo ya existe en la ruta especificada. No se realizó ninguna acción.")