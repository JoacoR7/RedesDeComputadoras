import tramasService
import utils

text = utils.leerArchivo('/home/joaco/Escritorio/Redes de Computadoras/TPS/TP 1/Tramas_802-15-4.log')

tramas = tramasService.separarTramas(text)

print("En total hay", len(tramas), "tramas")

tramasFiltradas = tramasService.contarTramasCorrectas(tramas)

print("En total hay", len(tramasFiltradas[0]), "tramas con correcta longitud")

tramasCorrectas = tramasService.verificarTramas(tramasFiltradas[0])[0]

print("En total hay", len(tramasCorrectas), "tramas con suma de verificación correcta y", (len(tramasFiltradas[0]) - len(tramasCorrectas)), "tramas con suma de verificación incorrecta.")

print("Hay", tramasService.contarSecuenciasDeEscape(tramas), "tramas que utilizan secuencia de escape")