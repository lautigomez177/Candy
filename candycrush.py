import random

def generar_matriz(lista):
    for i in range(len(lista)):
        for j in range(7):

            numero = random.randint(1,3)
            lista[i]["piezas"].append(numero)

    return lista

lista = [
{"piezas":[]},
{"piezas":[]},
{"piezas":[]},
{"piezas":[]}
]

listab = generar_matriz(lista)

for i in range(len(listab)):
    print(listab[i]["piezas"])