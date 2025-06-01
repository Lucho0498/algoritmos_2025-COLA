from queue import Queue
personajes = Queue()
personajes.arrive({"nombre": "Tony Stark", "personaje": "Iron Man", "genero": "M"})
personajes.arrive({"nombre": "Steve Rogers", "personaje": "Capitán América", "genero": "M"})
personajes.arrive({"nombre": "Natasha Romanoff", "personaje": "Black Widow", "genero": "F"})
personajes.arrive({"nombre": "Bruce Banner", "personaje": "Hulk", "genero": "M"})
personajes.arrive({"nombre": "Carol Danvers", "personaje": "Capitana Marvel", "genero": "F"})
personajes.arrive({"nombre": "Peter Parker", "personaje": "Spider-Man", "genero": "M"})
personajes.arrive({"nombre": "Wanda Maximoff", "personaje": "Scarlet Witch", "genero": "F"})
personajes.arrive({"nombre": "Scott Lang", "personaje": "Ant Man", "genero": "M"})



def NombreDeLaCapMarvel(personajes):
    colaAux =  Queue()
    while personajes.size() > 0:
        personaje= personajes.attention()
        if personaje['personaje'] == 'Capitana Marvel':
            print(personaje['nombre'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())


def MostrarNombresDePersonajesFem(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje['genero'] == 'F':
            print(personaje['nombre'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def MostrarNombresDePersonajesMas(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje['genero'] == 'M':
            print(personaje['nombre'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def MostrarNombreDeAntMan(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje['nombre'] == 'Scott Lang':
            print(personaje['personaje'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def PersonajesConLetraS(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje['nombre'][0] == 'S':
            print(personaje['nombre'], personaje['personaje'], personaje['genero'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())
        
def EncontrarCarolDanvers(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje['nombre'] == 'Carol Danvers':
                print("nombre: ",personaje['nombre'], "personaje: ", personaje ['personaje'], "genero: ", personaje['genero'])
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())
                
    


print('nombre de la Capitana Marvel:')
NombreDeLaCapMarvel(personajes)

print()

print('personajes femeninos:')
MostrarNombresDePersonajesFem(personajes)

print()

print('personajes masculinos:')
MostrarNombresDePersonajesMas(personajes)

print()

print('nombre del personaje de Scott Lang:')
MostrarNombreDeAntMan(personajes)

print()

print('personajes que empiezan con S:')
PersonajesConLetraS(personajes)

print()

print('Datos de Carol Danvers:')
EncontrarCarolDanvers(personajes)



