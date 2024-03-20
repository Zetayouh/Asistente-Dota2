from PIL import ImageTk, Image

#funcion para redimensionar imagenes
def redimensiona(self, imagen, medidas):
    resized = imagen.resize(medidas, Image.Resampling.HAMMING) #Redimensiona la imagen
    return ImageTk.PhotoImage(resized) #Devuelve la imagen redimensionada