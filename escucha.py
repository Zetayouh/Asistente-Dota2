from time import time
from speech_recognition import Recognizer, Microphone, UnknownValueError

from lector_de_texto import engine
from actualizacion_de_tiempos import *
from reestablecer import *
from cuenta_atras import *

#Funcion para establecer la hora de inicio
def establece_inicio(self, respuesta):
    retraso_marcacion = 2.3 #Se establece el tiempo de retraso de la marcación
    segundos_actuales = int(respuesta) + retraso_marcacion #Se suma el retraso a los segundos qu se la han dicho
    self.hora_inicio = (time() - segundos_actuales) #Establece la hora de inicio
    self.salir = False #Establece el parametro salir en False

#Función de reconocimiento de voz
def reconoce_voz(self):
        diccionario_numeros = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9} #Diccionario para traducir los numeros que detecta como palabras
        
        r = Recognizer() #Asigna el reconocedor a una variable
        with Microphone() as source: #Utilizando el microfono
            audio = r.listen(source) #Reconoce voz
            
        try:
            texto = r.recognize_google(audio, language='es') #Almacena en texto lo reconocido en lenguaje español

            if "empieza la partida" in texto: #Si detecta la frase "empieza la partida"
                reestablece_valores(self) #Reestablece valores de inicio
                engine.say("Qué segundo es?") #Pregunta "que segundo es"
                engine.runAndWait() #Espera respuesta
                engine.stop()
                with Microphone() as source: #Utilizando el microfono
                    audio = r.listen(source) #Reconoce voz
                
                try:
                    respuesta = r.recognize_google(audio, language='es') #Almacena en texto(segundos) lo reconocido en lenguaje español
                    
                    if "menos" in respuesta: #Si la palabra "menos" esta en la respuesta
                        palabras = respuesta.split(" ") #Separa las palabras
                        if palabras[1] in diccionario_numeros: #Si la palabra esta en el diccionario
                            palabras[1] = diccionario_numeros[palabras[1]] #La combierte en numero

                        retraso_marcacion = 2.3 #Establece el retraso de marcación
                        segundos_actuales = int(palabras[1]) - retraso_marcacion #Establece los segundos actuales de juego
                        self.hora_inicio = (time() + segundos_actuales) #Establece la hora de inicio
                        self.salir = False #Establece el parametro salir en False
                        cuenta_atras(self) #Empieza la cuenta atras

                    if respuesta in diccionario_numeros: #Si la palabra esta en el diccionario
                        respuesta = diccionario_numeros[respuesta] #La combierte en numero
                        establece_inicio(self, respuesta) #Llama a la funcion de establecer inicio
                        actualizar_tiempos(self) #Llama a la funcion de actualizar los tiempos
                        
                    else:
                        establece_inicio(self, respuesta) #Llama a la funcion de establecer inicio
                        actualizar_tiempos(self) #Llama a la funcion de actualizar los tiempos

                #Captura de errores
                except UnknownValueError: 
                    print("No se pudo reconocer el audio")

                except ValueError:
                    print("El audio no contiene un número válido")

            elif "salir" in texto: #Si reconoce la palabra "salir"
                self.salir = True
                #reestablece_valores(self) #Llama a la funcion de reestablecer valores
                
            elif "torturador aliado" in texto: #Si reconoce las palabras "torturador aliado"
                self.tormentor = True #Establece el parametro torturador en True
                self.inicio_tormentor = time() - self.tiempo_pausa #Establece el inicio del torturador
            
            elif "torturador enemigo" in texto: #Si reconoce la palabra "torturador enemigo"
                self.tormentor_e = True #Establece el parametro torturador_e en True
                self.inicio_tormentor_e = time() - self.tiempo_pausa #Establece el inicio del torturador enemigo

            elif "muerto" in texto: #Si reconoce la palabra "muerto"
                self.roshan = True #Establece el parametro roshan en True
                self.inicio_rosh = time() - self.tiempo_pausa #Establece el inicio del roshan
                self.numero_roshan += 1 #Suma 1 cada vez que detecta la palabra
                if self.numero_roshan < 4: #Si la cantidad es menor que 4
                    self.labels_objetos[self.numero_roshan].config(image=self.imagenes[self.numero_roshan]) #Añade la imagen del objeto correspondiente en el label correspondiente

            elif "pausa" in texto: #Si reconoce la palabra "pausa"
                #Invierte el estado del parametro pausa
                if self.pausa == False: 
                    self.pausa = True 
                elif self.pausa == True:
                    self.pausa = False 

        #Captura de error
        except:
            print("No se pudo reconocer el audio")