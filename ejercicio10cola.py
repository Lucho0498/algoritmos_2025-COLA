from queue import Queue
class notificacionesAplicaciones:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje
    def __str__(self):
        return f"Hora: {self.hora}, Aplicacion: {self.aplicacion}, Mensaje: {self.mensaje}"
    
notificaciones = Queue ()
notificaciones.arrive(notificacionesAplicaciones('10:00', 'Facebook', 'Nuevo comentario en tu foto'))
notificaciones.arrive(notificacionesAplicaciones('10:05', 'Twitter', 'Nuevo seguidor'))
notificaciones.arrive(notificacionesAplicaciones('10:10', 'Facebook', 'Alguien reaccionó a tu publicación'))
notificaciones.arrive(notificacionesAplicaciones('11:30', 'TikTok', 'Nuevo comentario en tu video'))
notificaciones.arrive(notificacionesAplicaciones('13:27', 'Instagram', 'Alguien reaccionó a tu publicación'))
notificaciones.arrive(notificacionesAplicaciones('15:30', 'Twitter', 'Alguien reaccionó a tu publicación'))
notificaciones.arrive(notificacionesAplicaciones('16:10', 'Instagram','A este usuario le gustó tu historia'))




def eliminarNotificacionesFacebook(notificaciones):
    colaAux =  Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if notificacion.aplicacion != 'Facebook':
            colaAux.arrive(notificacion)

    return colaAux


def MostrarNotificacionesTwitter(notificaciones):
    colaAux = Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if notificacion.aplicacion == "Twitter":
            print(notificacion.mensaje)
        colaAux.arrive(notificacion)
    
    while colaAux.size() > 0:
        notificaciones.arrive(colaAux.attention())

def AlmacenarNotificacionSegunHora(notificaciones):
    colaAux = Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if '11:45' <= notificacion.hora <= '15:57':
            colaAux.arrive(notificacion)
    
    while colaAux.size() > 0:
        notificaciones.arrive(colaAux.attention())
        notificaciones.show()



print("notificaciones de Twitter:")
MostrarNotificacionesTwitter(notificaciones)

print("Eliminando notificaciones de Facebook:")
notificaciones = eliminarNotificacionesFacebook(notificaciones)

print('notificaciones entre la 11:45 a 15:57')
AlmacenarNotificacionSegunHora(notificaciones)