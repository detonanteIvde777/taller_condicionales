# programa para saver si un numero es entero

# input
print("-------------------------")
print("-----numero par/impar----")
print("-------------------------")
x = int(input("digite un numero: "))

# processing
mod = x%2
if (mod == 0):
    rta = "par"
else:
    rta = "impar"

# output
print("--------------------------")
print("------resultado-----------")
print("--------------------------")
print("el numero " + str(x) + " es " + rta)