from time import time, strftime, gmtime
import threading

from aviso_por_voz import *
from reestablecer import *

def ajusta_tier(self):
    if self.tier_objetos < 5:
        if self.tiempo_transcurrido > self.lista_tiempos[self.tier_objetos -1] * 60 and self.salir == False:
            
            self.tier_objetos +=1
            self.label_obj_jungla.config(text="Objetos de tier {} disponibles en ".format(self.tier_objetos))
            ajusta_tier(self)

# Función para actualizar los labels con los tiempos transcurridos
def actualizar_tiempos(self):
    try:
        if self.pausa == True: #Si se pausa la partida
            self.tiempo_pausa += 1 #Aumenta el tiempo de pausa
            
        if self.pausa == False: #Si no esta pausada
            self.tiempo_transcurrido = round(time() - self.hora_inicio - self.tiempo_pausa) #Transcurre el tiempo
            tiempo_formateado = strftime("%H:%M:%S", gmtime(self.tiempo_transcurrido)) #Formatea el tiempo
            self.label_tiempo.config(text=tiempo_formateado) #Muestra el tiempo en el label principal
            
            ajusta_tier(self)

            if self.tier_objetos <= 5:
                tiempo_obj_jungla = round((self.lista_tiempos[self.tier_objetos - 1] * 60) - self.tiempo_transcurrido)
                tiempo_obj_jungla_formateado = strftime("%H:%M:%S", gmtime(tiempo_obj_jungla))
                self.label_tiempo_obj_jungla.config(text=tiempo_obj_jungla_formateado)
                if tiempo_obj_jungla == 35 and self.mute_4.get() == 0:
                    t = threading.Thread(target=dice, args=(self, self.label_tiempo_obj_jungla, tiempo_obj_jungla, "objeto"))
                    t.start()
                if tiempo_obj_jungla < 1:
                    self.tier_objetos += 1
                    if self.tier_objetos <= 5:
                        self.label_obj_jungla.config(text="Objetos de tier {} disponibles en ".format(self.tier_objetos))

            for label, tiempo in self.labels_tiempos.items(): #Por cada temporizador de runa y su correspondiente tiempo
                tiempo_restante = round(tiempo - (self.tiempo_transcurrido % tiempo)) #Establece el tiempo que falta
                resto_formateado = strftime("%H:%M:%S", gmtime(tiempo_restante)) #Lo formatea
                label.config(text=f"{resto_formateado}") #Lo muestra en el label correspondiente

                #Establece un tiempo de aviso para cada tipo de runa y llama a la funcion "dice" a traves de un hilo, siempre que no este muteado
                if label == self.label_tiempo_runas_rio and tiempo_restante == 15 and self.mute_1.get() == 0:
                    t = threading.Thread(target=dice, args=(self, label, tiempo_restante, "runa"))
                    t.start()
                if label == self.label_tiempo_runas_bounty and tiempo_restante == 20 and self.mute_2.get() == 0:
                    t = threading.Thread(target=dice, args=(self, label, tiempo_restante, "runa"))
                    t.start()
                if label == self.label_tiempo_runas_exp and tiempo_restante == 30 and self.mute_3.get() == 0:
                    t = threading.Thread(target=dice, args=(self, label, tiempo_restante, "runa"))
                    t.start()

            #Establece el dia
            if (self.tiempo_transcurrido / 300) % 2 < 1:
                self.es_dia = True
            
            #Establece la noche
            if (self.tiempo_transcurrido / 300) % 2 >= 1:
                self.es_dia = False
                
            if self.es_dia: #Si es de dia
                self.label_flecha.config(image=self.flecha_abajo_imagen) #Asigna la flecha abajo

            if self.es_dia == False: #Si no es de dia
                self.label_flecha.config(image=self.flecha_arriba_imagen) #Asigna la flecha arriba
            
            if self.numero_roshan >= 3: # Si es el 4º Roshan o mas
                    if self.es_dia: #Si es de dia
                        self.labels_objetos[3].config(image=self.imagenes[3]) #Establece imagen de Aghanin
                    else: #Y si no es de dia
                        self.labels_objetos[3].config(image=self.imagenes[4]) #Establece imagen de Refresher

            #Activacion del temporizador de Roshan
            if self.roshan == True: #Si Roshan esta activo
                tiempo_rosh = round(480 + self.inicio_rosh) - (self.hora_inicio + self.tiempo_transcurrido) #Transcurre el tiempo
                tiempo_rosh_formateado = strftime("%H:%M:%S", gmtime(tiempo_rosh)) #Lo formatea
                self.label_tiempo_rosh.config(text=f"{tiempo_rosh_formateado}") #Lo muestra en el label
                if tiempo_rosh == 17 and self.mute_6.get() == 0: #Se establece el tiempo de margen
                    dice(self, self.label_rosh, tiempo_rosh, "rosh") #Inicia el aviso por voz
                    self.roshan = False #Se desactiva Roshan

            #Cuenta atras inicales de los torturadores
            if self.tiempo_transcurrido < 1200: 
                tiempo_tormentor = round(1200 - (self.tiempo_transcurrido % 1200))
                tiempo_tormentor_formateado = strftime("%H:%M:%S", gmtime(tiempo_tormentor))
                self.label_tiempo_tormentor.config(text=f"{tiempo_tormentor_formateado}")
                self.label_tiempo_tormentor_e.config(text=f"{tiempo_tormentor_formateado}")
                if tiempo_tormentor == 17 and self.mute_5.get() == 0:
                    t = threading.Thread(target=dice, args=(self, self.label_tormentor, tiempo_tormentor, "tormentors"))
                    t.start()
                        
                if tiempo_tormentor == 0:
                    tiempo_tormentor_formateado = strftime("%H:%M:%S", gmtime(tiempo_tormentor))
                    self.tormentor = False

            #Cuenta atras de torturador aliado 
            if self.tormentor == True:
                tiempo_tormentor = round(600 + self.inicio_tormentor) - (self.hora_inicio + self.tiempo_transcurrido)
                tiempo_tormentor_formateado = strftime("%H:%M:%S", gmtime(tiempo_tormentor))
                self.label_tiempo_tormentor.config(text=f"{tiempo_tormentor_formateado}")
                if tiempo_tormentor == 17 and self.mute_5.get() == 0:
                    t = threading.Thread(target=dice, args=(self, self.label_tormentor, tiempo_tormentor, "tormentor"))
                    t.start()
                if tiempo_tormentor == 0:
                    self.tormentor = False

            #Cuenta atras de torturador enemigo    
            if self.tormentor_e == True:
                tiempo_tormentor_e = round(600 + self.inicio_tormentor_e) - (self.hora_inicio + self.tiempo_transcurrido)
                tiempo_tormentor_e_formateado = strftime("%H:%M:%S", gmtime(tiempo_tormentor_e))
                self.label_tiempo_tormentor_e.config(text=f"{tiempo_tormentor_e_formateado}")
                if tiempo_tormentor_e == 17 and self.mute_6.get() == 0:
                    t = threading.Thread(target=dice, args=(self, self.label_tormentor_e, tiempo_tormentor_e, "tormentor"))
                    t.start()
                if tiempo_tormentor_e == 0:
                    self.tormentor_e = False
        
        if self.salir == False: #Si salir es falso
            self.root.after(1000, lambda: actualizar_tiempos(self)) #Vuelve a ejecutar la funcion al de 1seg

        else: #Si salir es verdadero
            reestablece_valores(self) #Reinicio de valores

    except:
        reestablece_valores(self) #Reinicio de valores