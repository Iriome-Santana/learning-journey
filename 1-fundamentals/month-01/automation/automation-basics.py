import os
import shutil

HOME = os.path.expanduser("~")
DESCARGAS = os.path.join(HOME, "Downloads")

TIPOS = {"pdf": "Documentos", "png": "Imagenes", "jpg": "Imagenes", "docx": "Documentos", "txt": "Documentos"}

for archivo in os.listdir(DESCARGAS):
    ruta_archivo = os.path.join(DESCARGAS, archivo)
    
    if os.path.isfile(ruta_archivo):
        extension = archivo.split(".")[-1]
        
        if extension in TIPOS:
            carpeta_destino = os.path.join(HOME, TIPOS[extension])
            
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
            
        