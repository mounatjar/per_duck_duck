import sys

lista = ["Mounat", "Paola", "Sofia"]
numero = int(input("Introduzca el número del jugador: "))

def duck(lista,numero):
    if numero <= len(lista):
        jugador = lista[numero + 1]
        return jugador
    else:
        return "No hay tantos jugadores"
print("El resultado es: ", duck(lista,numero))

#hola q tal    
