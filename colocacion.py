from tkinter import Label, Checkbutton

from control_mute import *

#Creación de labels
def colocar_label(self, texto, fuente=("Arial", 30)):
    return Label(self.root, text=texto, font=fuente)

#Creación de checkbuttons
def colocar_checkbutton(self, var, num):
    return Checkbutton(self.root, variable=var, onvalue=0, offvalue=1, image=self.active_imagen, command=lambda: mute_desmute(self, var, num))

#Colocación de imágenes de los checkbuttons
def coloca_imagenes(self):
    columna = 1
    for label in self.labels_img:
        label.grid(column=columna, row=8)
        label.config(background="black")
        columna+=1

#Colocación de todos los labels y checkbutons en el grid
def organizar_pantalla(self, filas, columnas):
    contador = 0
    for fila in range(1, filas + 1):
        for columna in range(columnas):
            if columna == 2:
                self.labels[contador].grid(row=fila, column=5, padx=10)
            else:
                if columna == 1:
                    self.labels[contador].grid(row=fila, column=2, columnspan=3, sticky="e")
            
                else:
                    self.labels[contador].grid(row=fila, column=columna, sticky="w")
                self.labels[contador].config(background="black", fg="white", justify="left", padx=10, pady=5)    
            contador+=1

#Creación de labels de ayuda
def colocar_label_ventanas(ventana, texto, fuente=("Arial", 25)):
    return Label(ventana, text=texto, font=fuente)

#Colocación de los labels de ayuda en el grid
def organizar_ventana_ayuda(labels, filas, columnas):
    contador = 0
    for fila in range(filas):
        for columna in range(columnas):
                labels[contador].grid(row=fila, column=columna, sticky="w")
                if fila == 1:
                    labels[contador].config(background="black", fg="yellow", padx=10, pady=5)
                else:
                    labels[contador].config(background="black", fg="white", padx=10, pady=5)
                contador+=1
