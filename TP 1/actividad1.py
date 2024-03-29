import tramasService
import utils

text = utils.leerArchivo('./TP 1/Tramas_802-15-4.log')

tramas = tramasService.separarTramas(text)

print("En total hay", len(tramas), "tramas")

tramasConLongitudCorrecta, tramasConLongitudIncorrecta = tramasService.contarTramasLongitudCorrecta(tramas)

print(tramasConLongitudIncorrecta)

print("En total hay", len(tramasConLongitudCorrecta), "tramas con correcta longitud")

tramasCorrectas = tramasService.contarTramasChecksumCorrecto(tramasConLongitudCorrecta)[0]

print("En total hay", len(tramasCorrectas), "tramas con suma de verificación correcta y", (len(tramasConLongitudCorrecta) - len(tramasCorrectas)), "tramas con suma de verificación incorrecta.")

print("Hay", tramasService.contarSecuenciasDeEscape(tramas), "tramas que utilizan secuencia de escape")

tramasConSecuenciaDeEscape = tramasService.localizarTramas(tramasService.detectarSecuenciaEscape, tramas)

print("Las siguientes líneas contienen tramas con secuencia de escape:")
for linea in tramasConSecuenciaDeEscape:
    print(linea, ":", tramasService.filtrarSecuenciaEscape(tramas[linea]))

tramasConLongitudIncorrecta = tramasService.localizarTramas(tramasService.validarLongitudTrama, tramas)

print("Las siguientes líneas contienen tramas con longitud incorrecta:")
for linea in tramasConLongitudIncorrecta:
    print(linea, ":", tramas[linea])

tramasConChecksumIncorrecto = tramasService.localizarTramas(tramasService.checkSum, tramas)

print("Las siguientes líneas contienen tramas con checksum incorrecto:")
for linea in tramasConChecksumIncorrecto:
    print(linea, ":", tramas[linea])