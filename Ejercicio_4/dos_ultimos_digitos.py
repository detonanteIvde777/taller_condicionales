# programa para verificar si los dos ultimos digitos son iguales

# input
print("-------------------------")
print("-----ultimos digitos iguales----")
print("-------------------------")
x = int(input("digite un numero: "))

# processing
ultimo_digito = x % 10
penultimo_digito = (x//10)%10
if (ultimo_digito == penultimo_digito):
    rta = "iguales"
else:
    rta = "diferentas"

# output
print("--------------------------")
print("--------resultado-----------")
print("---------------------------")
print("el numero ingresado fue: " + str(x))
print("su ultimo digito es: " + str(ultimo_digito))
print("su penultimo degito es: " +  str(penultimo_digito))
print("los dos ultimos digitos son " + rta)