# programa para calcular si un numero es pocitivo

# input
print("-------------------------")
print("-----numero positivo-----")
print("-------------------------")
x = int(input("digite un numero: "))

# processing
if (x>0):
    rta = "positivo"
else:
    rta = "NEGATIVO O SERO"

# output
print("--------------------------")
print("------resultado-----------")
print("--------------------------")
print("el numero " + str(x) + " es " + rta)
