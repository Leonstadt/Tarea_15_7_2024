#Calcular el IVA de un valor (15%) y presentar
V=float(input("ingrese el valor a calcularle el IVA: "))
IVA=(V*0.15)
R=IVA+V
print(f"El IVA de {V} es {IVA}, dando un total a pagar de: {R}")
