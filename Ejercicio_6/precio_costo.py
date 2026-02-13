# programa en python para calcular el precio costo de un producto

# Libreria
import math

#------
#input
#-------

print("-------------------------")
print("   calcular precio venta de un producto")
print("-------------------------")

pc=int(input("digite el precio costo del producto: "))

#---------
#processing
#---------

if(pc<3000):
    pv=(pc*0.15)+pc

else:
    if(pc>6000): 
        pv=(pc*0.25)+pc

    else:
        pv=pc+500

#----------
#output
#----------

print("-------------------------")
print("--------resultados-------")
print("el precio de venta es: " +str(pv))
print("-------------------------")



