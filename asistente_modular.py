from tkinter import Tk, Menu, IntVar
from pynput import keyboard
from PIL import Image

from colocacion import *
from escucha import *
from trabajo_de_imagenes import *
from ayuda_al_usuario import abrir_ventana_ayuda
from ventana_de_asignacion import abrir_ventana_asignación

root=Tk()

class Asistente:
    def __init__(self, root):
        #Parametros del root
        self.root = root
        self.root.title("Asistente Dota 2")
        self.root.iconbitmap(r'Logo.ico') 
        self.barra_menu = Menu(root)
        self.root.config(menu=self.barra_menu, background="black")
        
        #Barra de menu
        #Menu de Configuración
        self.configuracion_menu = Menu(self.barra_menu, tearoff=0)
        self.configuracion_menu.add_command(label="Asignación de tecla", command=lambda: abrir_ventana_asignación(self))
        self.barra_menu.add_cascade(label="Configuración", menu=self.configuracion_menu)

        #Menu de Ayuda
        self.ayuda_menu = Menu(self.barra_menu, tearoff=0)
        self.ayuda_menu.add_command(label="Información de uso", command=lambda: abrir_ventana_ayuda(self))
        self.barra_menu.add_cascade(label="Ayuda", menu=self.ayuda_menu)

        #Activación de escucha al pulsar tecla
        self.listener = keyboard.Listener(on_press=self.al_pulsar_tecla)
        self.listener.start()

        #Variables generales
        self.hora_inicio = 0
        self.tiempo_transcurrido = 0
        self.roshan = False
        self.inicio_rosh = 0
        self.tormentor = False
        self.inicio_tormentor = 0
        self.tormentor_e = False
        self.inicio_tormentor_e = 0
        self.pausa = False
        self.tiempo_pausa = 0
        self.salir = False
        self.numero_roshan = 0
        self.es_dia = ""
        self.descuento = True
        self.tecla_hablar = keyboard.Key.ctrl_r
        self.nombre_tecla = self.tecla_hablar.name
        self.tier_objetos = 1
        
        
        #Imagenes
        self.active_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\active.png")), (35, 35))
        self.mute_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\mute.png")), (35, 35))
        
        self.flecha_arriba_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\flecha_arriba.png")), (60, 60))
        self.flecha_abajo_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\flecha_abajo.png")), (60, 60))

        self.aegis_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\aegis.png")), (60, 60))
        self.queso_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\queso.png")), (60, 60))
        self.estandarte_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\estandarte.png")), (60, 60))
        self.aghanim_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\aghanims.png")), (60, 60))
        self.refresher_imagen = redimensiona(self, (Image.open(r"Imagenes Dota2\\refresher.png")), (60, 60))

        #Lista de imagenes de objetos de Roshan
        self.imagenes = [self.aegis_imagen, self.queso_imagen, self.estandarte_imagen, self.aghanim_imagen, self.refresher_imagen]

        #Variables de los checkbuttons y función de mute-desmute:
        self.mute_1 = IntVar()
        self.mute_2 = IntVar()
        self.mute_3 = IntVar()
        self.mute_4 = IntVar()
        self.mute_5 = IntVar()
        self.mute_6 = IntVar()
        self.mute_7 = IntVar()

        # Crear el label que mostrará el tiempo transcurrido
        self.label_tiempo = colocar_label(self, "00:00:00", ("Arial", 60))
        self.label_tiempo.grid(column= 0, row=0, columnspan=5)
        self.label_tiempo.config(background="black", fg="yellow", justify="center")

        # Fila 1
        self.label_runas_rio = colocar_label(self, "Runas de Rio en ")
        self.label_tiempo_runas_rio = colocar_label(self, "00:00:00")
        self.mute_runa_rio = colocar_checkbutton(self, self.mute_1, 0)

        #Fila 2
        self.label_runas_bounty = colocar_label(self, "Bountys y lotos en ")
        self.label_tiempo_runas_bounty = colocar_label(self, "00:00:00")
        self.mute_runa_bounty = colocar_checkbutton(self, self.mute_2, 1)

        #Fila 3
        self.label_runas_exp = colocar_label(self, "Runas de Exp en ")
        self.label_tiempo_runas_exp = colocar_label(self, "00:00:00")
        self.mute_runa_exp = colocar_checkbutton(self, self.mute_3, 2)

        #Fila 4
        self.label_obj_jungla = colocar_label(self, "Objetos de tier {} disponibles en ".format(self.tier_objetos))
        self.label_tiempo_obj_jungla = colocar_label(self, "00:00:00")
        self.mute_obj_jungla = colocar_checkbutton(self, self.mute_4, 3)

        #Fila 5
        self.label_tormentor = colocar_label(self, "Torturador aliado disponible en ")
        self.label_tiempo_tormentor = colocar_label(self, "00:00:00")
        self.mute_tormentor = colocar_checkbutton(self, self.mute_5, 4)

        #Fila 6
        self.label_tormentor_e = colocar_label(self, "Torturador enemigo disponible en ")
        self.label_tiempo_tormentor_e = colocar_label(self, "00:00:00")
        self.mute_tormentor_e = colocar_checkbutton(self, self.mute_6, 5)

        #Labels de rosh
        self.label_rosh = colocar_label(self, "Roshan puede revivir en ")
        self.label_rosh.grid(column=0, row=7, sticky="w")
        self.label_rosh.config(background="black", fg="white", justify="left", padx=10, pady=5)

        self.label_flecha = Label(self.root, image="")
        self.label_flecha.grid(column=1, row=7)
        self.label_flecha.config(background="black")

        self.label_tiempo_rosh = colocar_label(self, "00:00:00")
        self.label_tiempo_rosh.grid(column=2, row=7, columnspan=3, sticky="e")
        self.label_tiempo_rosh.config(background="black", fg="white", padx=10, pady=5)

        self.mute_rosh = colocar_checkbutton(self, self.mute_7, 6)
        self.mute_rosh.grid(row=7, column=5, padx=10)

        self.label_objetos_rosh = colocar_label(self, "Objetos de Roshan disponibles: ")
        self.label_objetos_rosh.grid(column=0, row=8, sticky="w")
        self.label_objetos_rosh.config(background="black", fg="white", justify="left", padx=10, pady=5)

        #Labels imagenes rosh
        self.label_aegis = Label(self.root, image=self.imagenes[0])
        self.label_queso = Label(self.root, image="")
        self.label_estandarte = Label(self.root, image="")
        self.label_aghanim_refresh = Label(self.root, image="")
       
        #Lista de labels y organización de pantalla
        self.labels = [self.label_runas_rio, self.label_tiempo_runas_rio, self.mute_runa_rio, 
                    self.label_runas_bounty, self.label_tiempo_runas_bounty, self.mute_runa_bounty, 
                    self.label_runas_exp, self.label_tiempo_runas_exp, self.mute_runa_exp, 
                    self.label_obj_jungla, self.label_tiempo_obj_jungla, self.mute_obj_jungla, 
                    self.label_tormentor, self.label_tiempo_tormentor, self.mute_tormentor,
                    self.label_tormentor_e, self.label_tiempo_tormentor_e, self.mute_tormentor_e]
        organizar_pantalla(self, 6, 3)

        #Lista de labels de imagenes y su colocación
        self.labels_img = [self.label_aegis, self.label_queso, self.label_estandarte, self.label_aghanim_refresh]
        coloca_imagenes(self)

        #Listas y diccionarios
        self.lista_tiempos = [7, 17, 27, 37, 60]
        self.labels_relacion = {self.label_tiempo_runas_rio:self.label_runas_rio, self.label_tiempo_runas_bounty:self.label_runas_bounty, 
                                self.label_tiempo_obj_jungla:self.label_obj_jungla, self.label_tiempo_runas_exp:self.label_runas_exp}
        self.labels_tiempos = {self.label_tiempo_runas_rio:120, self.label_tiempo_runas_bounty:180, self.label_tiempo_runas_exp:420}
        self.labels_objetos = [self.label_aegis, self.label_queso, self.label_estandarte, self.label_aghanim_refresh]
        self.lista_checkbuttons = [self.mute_runa_rio, self.mute_runa_bounty, self.mute_runa_exp, self.mute_obj_jungla, self.mute_tormentor, self.mute_tormentor_e, self.mute_rosh]

    #Función de "push to talk" asignado en la tecla control derecho
    def al_pulsar_tecla(self, tecla):
        #print('Tecla presionada: {0}'.format(tecla))
        #print(self.tecla_hablar)
        if tecla == self.tecla_hablar: #Si la tecla pulsada es la tecla asignada a la función
            reconoce_voz(self) #Llama a la función de reconocimiento de voz

if __name__ == '__main__':
    mi_asistente = Asistente(root)
    root.mainloop()