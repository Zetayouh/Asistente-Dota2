from tkinter import Toplevel, Label, Button
from pynput import keyboard
from functools import partial

def abrir_ventana_asignación(self):

    #Funcion para cambiar el texto del boton al clickar sobre el
    def cambia_texto(self, boton):
        boton.config(text="Pulsa la tecla a asignar")

    #Funcion para cambiar la tecla predefinida
    def al_pulsar(tecla, self):
        self.tecla_hablar = tecla
        #Mostrar el nombre de la tecla en el boton
        try:
            self.nombre_tecla = tecla.name
        except:
            self.nombre_tecla = tecla.char
    
        cerrar_ventana() #Llama a la funcvion de cerrar ventana

    def cerrar_ventana():
        ventana_asignacion.destroy() #cierra la ventana

    #Creación de ventana de Asignacion de tecla
    ventana_asignacion = Toplevel()
    ventana_asignacion.title("Asignación de tecla")
    ventana_asignacion.config(background="black")
    
    #Creación de labels
    label_informativo = Label(ventana_asignacion, text="Push to talk", font=("Arial", 30))
    label_informativo.grid(column=0, row=0, sticky="w")
    label_informativo.config(background="black", fg="white", padx=10, pady=10)

    #Creación del boton de la tecla
    boton_cambio_tecla = Button(ventana_asignacion, text=self.nombre_tecla, width=17, font=("Arial", 30), command=lambda: cambia_texto(self, boton_cambio_tecla))
    boton_cambio_tecla.grid(column=1, row=0, sticky="e")
    boton_cambio_tecla.config(background="grey", padx=10, pady=10)

    #Captura de tecla pulsada y llamada a la función "al_pulsar"
    listener = keyboard.Listener(on_press=partial(al_pulsar, self=self))
    listener.start()

    ventana_asignacion.mainloop()