from queue import Queue
class PersonajesMarvel:
    def __init__(self, nombre, personaje, genero):
        self.nombre = nombre
        self.personaje = personaje
        self.genero = genero
    def __str__(self):
        return f"nombre: {self.nombre}, personaje: {self.personaje}, genero: {self.genero}"
personajes = Queue()
personajes.arrive(PersonajesMarvel("Tony Stark", "Iron Man", "M"))
personajes.arrive(PersonajesMarvel("Steve Rogers", "Capitán América", "M"))
personajes.arrive(PersonajesMarvel("Natasha Romanoff", "Black Widow", "F"))
personajes.arrive(PersonajesMarvel("Bruce Banner", "Hulk", "M"))
personajes.arrive(PersonajesMarvel("Carol Danvers", "Capitana Marvel", "F"))
personajes.arrive(PersonajesMarvel("Peter Parker", "Spider-Man", "M"))
personajes.arrive(PersonajesMarvel("Wanda Maximoff", "Scarlet Witch", "F"))
personajes.arrive(PersonajesMarvel("Scott Lang", "Ant Man", "M"))



def NombreDeLaCapMarvel(personajes):
    colaAux =  Queue()
    while personajes.size() > 0:
        personaje= personajes.attention()
        if personaje.personaje == 'Capitana Marvel':
            print(personaje.nombre)
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())


def MostrarNombresDePersonajesFem(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje.genero == 'F':
            print(personaje.nombre)
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def MostrarNombresDePersonajesMas(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje.genero == 'M':
            print(personaje.nombre)
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def MostrarNombreDeAntMan(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje.nombre == 'Scott Lang':
            print(personaje.personaje)
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())

def PersonajesConLetraS(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje.nombre[0] == 'S':
            print('nombre: ', personaje.nombre, 'personaje: ', personaje.personaje, 'genero: ', personaje.genero)
        colaAux.arrive(personaje)
    
    while colaAux.size() > 0:
        personajes.arrive(colaAux.attention())
        
def EncontrarCarolDanvers(personajes):
    colaAux = Queue()
    while personajes.size() > 0:
        personaje = personajes.attention()
        if personaje.nombre == 'Carol Danvers':
                print("nombre: ",personaje.nombre, "personaje: ", personaje.personaje, "genero: ", personaje.genero)
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



