import json
from funciones import *
id=os.environ["id"]
key=os.environ["key"]
print("Información del perfil Senutrio-Harivantan")
#Menú de opciones
menu='''
1. Mostrar Biblioteca de juegos
2. Horas de un videojuego
3. Información del perfil
4. Salir
'''
#Iniciar el programa
print(menu)
opcion = int(input("Seleccione una opción: "))
while opcion != 4:
    if opcion == 1:
        print("Biblioteca de juegos")
        for i in juegos_obtiene(key,id):
            print("-->",i)
        print()
    elif opcion == 2:
        juego=input("Ingrese el nombre del juego: ")
        print(juego)
        for i in ultimo_juego(key,id,juego):
            print(i/60,"horas")
    elif opcion == 3:
        print()
        print("---INFORMACIÓN USUARIO---")
        print("- SteamID: ",info_user(key,id)[0])
        print("- Nombre Real: ",info_user(key,id)[1])
        print("- País: ",info_user(key,id)[2])
    elif opcion == 4:
        print("Gracias por utilizar el programa")
    else:
        print("Opción no valida")
    print (menu)
    opcion = int(input("Seleccione una opción: "))

