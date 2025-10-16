class SalonVideojuego:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion

        self.lista_jugadores = []
        self.num_jugador=0
        

    def agregar_jugador(self,jugador):
        self.lista_jugadores.append(jugador)
        self.num_jugador+=1


    def mostrar_jugadores_dia(self):
        for i in self.lista_jugadores:
            print("-------------------------")
            print(f"nombre: {i.nombre}")
            print(f"juego: {i.juego}")
            print(f"puntaje {i.puntaje}")
    
    def numero_jugadores(self):
        print(f"numero de jugadores: {self.num_jugador}")
    
class Jugador:
    def __init__(self,nombre,juego,puntaje):
        self.nombre = nombre
        self.juego = juego
        self.puntaje = puntaje


retrocity = SalonVideojuego("RetroCity", "juanjose 1999")

jugador_1= Jugador("papu", "pacman", 1000)

retrocity.agregar_jugador(jugador_1)
retrocity.mostrar_jugadores_dia()
retrocity.numero_jugadores()

while True:
    opt=0
    print("1. agrear jugador.")
    print("2. mostrar jugadores del dia.")
    print("3. mostrar numero de jugadores.")
    print("4. salir.")

    opt=int(input("elige una opcion: "))
    while opt not in range(1, 4):
        print("Error")
        opt=int(input("elige una opcion: "))
    
    if opt == 1:
        nombre =input("nombre del jugador: ")
        juego =input("que juego juega: ")
        puntaje =input("puntaje que obtubo: ")
        jugador_2 = Jugador(nombre, juego,puntaje)
        retrocity.agregar_jugador(jugador_2)
    if opt ==2:
        retrocity.mostrar_jugadores_dia()
    if opt ==3:
        retrocity.numero_jugadores()
    if opt ==4:
        break