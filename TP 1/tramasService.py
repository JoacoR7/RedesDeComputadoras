def separarTramas(text):
    tramas = []
    trama = "7E"

    for i in range(2, len(text), 2):
        byte = text[i:i+2]
        if(byte != "7E"):
            trama = trama + byte
        else:
            if(text[i-2:i] == "7D"):
                trama = trama + byte
            else:
                tramas.append(trama)
                trama = "7E"

    return tramas

def validarLongitudTrama(trama):
    longitudOriginal = len(trama)/2 - 4
    longitud = int(trama[2:6], 16)
    return longitud != longitudOriginal



def contarTramasLongitudCorrecta(tramas):
    tramasCorrectas = []
    tramasIncorrectas = []

    for trama in tramas:
        if not validarLongitudTrama(trama):
            tramasCorrectas.append(trama)
        else:
            tramasIncorrectas.append(trama)
    
    return tramasCorrectas, tramasIncorrectas

def checkSum(trama):
    suma = 0
    for i in range(6, len(trama)-2, 2):
        suma = suma + int(trama[i:i+2], 16)
    return int(trama[len(trama)-2:len(trama)], 16) != int("FF", 16) - (suma & int("FF", 16))

def contarTramasChecksumCorrecto(tramas):
    tramasCorrectas = []
    tramasIncorrectas = []
    i = 0
    for trama in tramas:
        if not checkSum(trama):
            tramasCorrectas.append(trama)
        else:
            tramasIncorrectas.append(trama)
        i += 1
    
    return tramasCorrectas, tramasIncorrectas

def filtrarSecuenciaEscape(trama):
    trama = trama.replace("7D7E", "7E")
    return trama

def detectarSecuenciaEscape(trama):
    for i in range(2, len(trama) - 2, 2):
            if(trama[i:i+4] == "7D7E"):
                return True
    return False

def contarSecuenciasDeEscape(tramas):
    contador = 0
    for trama in tramas:
        if(detectarSecuenciaEscape(trama)):
            contador += 1
    return contador

def localizarTramas(func, tramas):
    linea = 0
    tramasLocalizadas = []
    for trama in tramas:
        if(func(trama)):
            tramasLocalizadas.append(linea)
        linea += 1
    return tramasLocalizadas


