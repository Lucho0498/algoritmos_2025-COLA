from queue import Queue

notificaciones = Queue ()
notificaciones.arrive({'hora': '10:00', 'aplicacion': 'Facebook', 'mensaje': 'Nuevo comentario en tu foto'})
notificaciones.arrive({'hora': '10:05', 'aplicacion': 'Twitter', 'mensaje': 'Nuevo seguidor'})
notificaciones.arrive({'hora': '10:10', 'aplicacion': 'Facebook', 'mensaje': 'Alguien reaccionó a tu publicación'})
notificaciones.arrive({'hora': '11:30', 'aplicacion': 'TikTok', 'mensaje': 'Nuevo comentario en tu video'})
notificaciones.arrive({'hora': '13:27', 'aplicacion': 'Instagram', 'mensaje': 'Alguien reaccionó a tu publicación'})
notificaciones.arrive({'hora': '15:30', 'aplicacion': 'Twitter', 'mensaje': 'Alguien reaccionó a tu publicación'})
notificaciones.arrive({'hora': '16:10', 'aplicacion': 'Instagram', 'mensaje': 'A este usuario le gustó tu historia'})




def eliminarNotificacionesFacebook(notificaciones):
    colaAux =  Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if notificacion['aplicacion'] != 'Facebook':
            colaAux.arrive(notificacion)

    return colaAux


def MostrarNotificacionesTwitter(notificaciones):
    colaAux = Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if notificacion['aplicacion'] == "Twitter":
            print(notificacion['mensaje'])
        colaAux.arrive(notificacion)
    
    while colaAux.size() > 0:
        notificaciones.arrive(colaAux.attention())

def AlmacenarNotificacionSegunHora(notificaciones):
    colaAux = Queue()
    while notificaciones.size() > 0:
        notificacion = notificaciones.attention()
        if '11:45' <= notificacion['hora'] <= '15:57':
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