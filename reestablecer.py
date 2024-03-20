#Reestablecimiento de valores
def reestablece_valores(self):
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
    self.salir = True
    self.numero_roshan = 0
    self.es_dia = ""
    self.descuento = True
    self.tier_objetos = 1

    #Reestablecer contadores a 0
    self.label_tiempo.config(text="00:00:00")
    self.label_tiempo_runas_rio.config(text="00:00:00")
    self.label_tiempo_runas_bounty.config(text="00:00:00")
    self.label_tiempo_runas_exp.config(text="00:00:00")
    self.label_tiempo_rosh.config(text="00:00:00")
    self.label_tiempo_tormentor.config(text="00:00:00")
    self.label_tiempo_tormentor_e.config(text="00:00:00")
    self.label_tiempo_obj_jungla.config(text="00:00:00")
    self.label_flecha.config(image="")
    self.label_obj_jungla.config(text="Objetos de tier 1 disponibles en ")

    #Reestablecer imagenes por defecto
    for label in self.labels_objetos:
        if label != self.label_aegis:
            label.config(image="")