from typing import List

modo = input("Pulse 1 para calculator el promedio individual o 2 para calcular el promedio total: ")

if modo!= "1" and modo!= "2":
    notas_7mo = []
    notas_8vo = []
    notas_9no = []


in_cant_7mo = int(input("di la cantidad de notas 7mo: "))
in_cant_8vo = int(input("di la cantidad de notas 8vo y 9no: "))
in_cant_9no = int(f'{in_cant_8vo}')

print("ahora pondras las notas de 7mo: ")
for i in range(in_cant_7mo):
    in1 = int(input('di las notas de 7mo: '))
    notas_7mo.append(in1)

print("ahora pondras las notas de 8vo: ")
for i in range(in_cant_8vo):
    in2 = int(input('di las notas de 8vo: '))
    notas_8vo.append(in2)

print("ahora pondras las notas de 9no:")
for i in range(in_cant_9no):
    in3 = int(input('di las notas de 9no: '))
    notas_9no.append(in3)

if modo == "1":
    Promedio_7mo = sum(notas_7mo)/len(notas_7mo)
    Promedio_8vo = sum(notas_8vo)/len(notas_8vo)
    Promedio_9no = sum(notas_9no)/len(notas_9no)

    print(f"El promedio de 7mo es: {Promedio_7mo}")
    print(f"El promedio de 8vo es: {Promedio_8vo}")
    print(f"El promedio de 9no es: {Promedio_9no}")

if modo == "2":
    Promedio_total = (sum(notas_7mo) + sum(notas_8vo) + sum(notas_9no)) / len(notas_7mo + notas_8vo + notas_9no)

    print(f"El promedio total es: {Promedio_total}")