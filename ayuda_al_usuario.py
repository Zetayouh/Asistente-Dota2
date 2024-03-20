from tkinter import Toplevel

from colocacion import *

def abrir_ventana_ayuda(self):
    #Creación de ventana de Ayuda
    ventana_ayuda = Toplevel()
    ventana_ayuda.title("Información de uso")
    ventana_ayuda.config(background="black", width=800, height=530)

    #Tecla asignada al push to talk
    

    #Labels de ayuda
    #Fila 1
    titulo_tecla = colocar_label_ventanas(ventana_ayuda, "Tecla para hablar: ")
    tecla_inicio = colocar_label_ventanas(ventana_ayuda, self.nombre_tecla+" (Asignado en configuración)")
    #Fila 2
    titulo_funcion = colocar_label_ventanas(ventana_ayuda, "Funciones: ", ("Arial", 35))
    titulo_comandos = colocar_label_ventanas(ventana_ayuda, "Comandos de voz:", ("Arial", 35))
    #Fila 3
    titulo_inicio = colocar_label_ventanas(ventana_ayuda, "Inicio de partida: ")
    explicacion_inicio = colocar_label_ventanas(ventana_ayuda, "'Empieza la partida'")
    #Fila 4
    titulo_segundos = colocar_label_ventanas(ventana_ayuda, "¿Qué segundo es?: ")
    respuesta_segundos = colocar_label_ventanas(ventana_ayuda, "'menos' + numero de segundo actual")
    #Fila 5
    titulo_pausa = colocar_label_ventanas(ventana_ayuda, "Pausar o reanudar partida: ")
    comando_pausa = colocar_label_ventanas(ventana_ayuda, "'Pausa'")
    #Fila 6
    titulo_torturador = colocar_label_ventanas(ventana_ayuda, "Activar torturador aliado: ")
    comando_torturador = colocar_label_ventanas(ventana_ayuda, "'Torturador aliado'")
    #Fila 7
    titulo_torturador_e = colocar_label_ventanas(ventana_ayuda, "Activar torturador enemigo: ")
    comando_torturador_e = colocar_label_ventanas(ventana_ayuda, "'Torturador enemigo'")
    #Fila 8
    titulo_roshan = colocar_label_ventanas(ventana_ayuda, "Activar Roshan: ")
    comando_roshan = colocar_label_ventanas(ventana_ayuda, "'Roshan ha muerto'")
    #Fila 9
    titulo_salir = colocar_label_ventanas(ventana_ayuda, "Salir de la partida: ")
    comando_salir = colocar_label_ventanas(ventana_ayuda, "'Salir'")

    #Lista de labels
    lista_labels = [titulo_tecla, tecla_inicio, titulo_funcion, titulo_comandos, titulo_inicio, explicacion_inicio, titulo_segundos, respuesta_segundos, 
                    titulo_pausa, comando_pausa, titulo_torturador, comando_torturador, titulo_torturador_e, comando_torturador_e, 
                    titulo_roshan, comando_roshan, titulo_salir, comando_salir]
    
    #LLamada a la funcion de organizar la ventana
    organizar_ventana_ayuda(lista_labels, 9, 2)