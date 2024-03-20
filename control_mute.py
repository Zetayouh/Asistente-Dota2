#Función para modificar la imagen del mute
def mute_desmute(self, var, num):
    if var.get() == 1: #Si el valor de la variable es 1
        self.lista_checkbuttons[num].config(image=self.mute_imagen) #Establece la imagen de mute
    else: #Sino
        self.lista_checkbuttons[num].config(image=self.active_imagen) #Establece la imagen de active