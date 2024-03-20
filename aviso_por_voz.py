from lector_de_texto import engine

#Función de avisos por voz
def dice(self, label, count, tipo):
    #Seleciona el texto y el tiempo que dirá
    if tipo == "rosh":
        texto = "Roxan puede revivir en " + str(count - 2) + " segundos"
    elif tipo == "tormentors":
        texto = "Torturadores disponibles en " + str(count - 2) + " segundos"
    elif tipo == "tormentor":
        texto = "Torturador disponible en " + str(count - 2) + " segundos"
    elif tipo == "runa" or tipo == "objeto":
        label_actual = self.labels_relacion[label]
        texto = label_actual.cget("text") + str(count - 2) + " segundos"
    
    #Intenta decirlo
    try:
        engine.say(texto)
        engine.runAndWait()
        engine.stop()   

    #Captura de posible error
    except:
        print("Loop activo")