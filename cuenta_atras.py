from time import time, strftime, gmtime

from actualizacion_de_tiempos import *

#Función de ejecución de la cuenta atrás inicial
def cuenta_atras(self):
    try:
        self.tiempo_transcurrido = self.hora_inicio - time() #Establece la variable de tiempo transcurrido
        tiempo_formateado = strftime("%H:%M:%S", gmtime(self.tiempo_transcurrido)) #Formatea el tiempo
        self.label_tiempo.config(text=tiempo_formateado) #Muestra el tiempo en el label

        if self.tiempo_transcurrido <= 1: #Condicion de finalización de la cuenta atrás
            self.hora_inicio = time() #Reestablece la hora de inicio
            self.descuento = False  #Finaliza el tiempo de descuento

        if self.descuento == True: #Mientras sea tiempo de descuento
            self.root.after(1000, lambda: cuenta_atras(self)) #Reejecuta la función tras 1seg

        if self.descuento == False: #Cuando la cuenta atrás finaliza
            actualizar_tiempos(self) #Comienza el contador de la partida
    
    except:
        reestablece_valores(self)