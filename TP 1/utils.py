import re

def leerArchivo(directorio):

    try:
        file = open(directorio, 'r') 

        text = file.readline()

    except:
            print("Error al leer el archivo")
    
    return text