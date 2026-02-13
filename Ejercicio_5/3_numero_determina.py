# programa para saver entre tres numeros cual es el meyor

#libreria
import math

#----------
#imput
#----------

print("-----------------------------")
print("----- verificar cual de los 3 numeros es el mayor-----")
print("-----------------------------")

A=int(input("digite el valor de A: "))
B=int(input("digite el valor de B: "))
C=int(input("digite el valor de C: "))

#----------
#processing
#----------

if(A>C):
    if(A>C):
        rta=A
    else:
        rta=C
else:
    if(B>C):
        rta=B
    else:
        rta=C

#-------
#ouput
#-------

print("---------------------------")
print("------ RESULTADOS----------")
print("---------------------------")
print("el valor de A es: " +str(A))
print("el valor de B es: " +str(B))
print("el valor de C es: " +str(C))
print("---------------------------")
print("el numero mas grande es: " +str(rta))
print("---------------------------")
