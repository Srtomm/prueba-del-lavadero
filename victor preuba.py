class Auto:
    def __init__(self,marca, modelo, patente,dueño):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.dueño = dueño
    def guardar_auto(self,biblio):
        biblio[self.patente]=[self.dueño,self.marca,self.modelo]




def mostrar_dia():
    print(f"autos lavados: {autos_dia}")
    
    

def mostrar_jornada():
    for i in autos_jornada.keys():
        print("--------------")
        print(f"patente: {i}")
        for e in autos_jornada[123]:
            print(e)
def agregar_auto():
    patente=input("cual es la patente: ")
    dueño=input("cual es la dueño: ")
    marca=input("cual es la marca: ")
    modelo=input("cual es la modelo: ")

    auto_1 = Auto(marca,modelo,patente,dueño)
    auto_1.guardar_auto(autos_jornada)



#menu
autos_jornada={123:["papu","ford","fiesta"]}
autos_dia=1
opc= 0

while True:
    print("1: cuantos autos atendido en el dia")
    print("2: lista de autos atendidos en la jornada")
    print("3: agregar auto")
    print("4: salir")
    opc= int(input("elige un opcion:"))
    while opc not in range(1,4):
        print("error")
        opc= int(input("elige un opcion:"))

    if opc== 1:
        mostrar_dia()
    elif opc==2:
        mostrar_jornada()
    elif opc==3:
        agregar_auto()
        opc+=1
        print(autos_jornada)
    else:
        break


    
