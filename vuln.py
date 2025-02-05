import os
from os import *


print("Este programa es el pack Inicial de uso de la computadora, sirve para abrir todo lo necesario")

print("Vamos a usar una funcion de interacción con el sistema para abrirlo, no cierres el terminal")


os.system("python3 -m http.server 3500 0>/dev/null 1>/dev/null 2>/dev/null &")
os.system("clear")
os.system("firefox &")
os.system("clear")

q = input("Te gusta este programa(S/N)")
if q == "s" or "S":
    print("Me alegro")
elif q == "n" or "N":
    input("Porque?")
    print("Me la suda")

#Para matar el proceso en consola de linux buscalo en el "ps aux", busca el servidor,
#copia el numero de proceso y con el comando "kill y el numero" lo terminas