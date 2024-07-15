#ingresamos edad y numero de articulos, luego presentamos con booleano si es >18 y >1 articulo
E=int(input("Ingrese su edad: "))
A=int(input("Ingrese el número de artículos: "))
B=(E>18 and A>1)
print(f"Tiene {E} años, Compró {A} articulos")
print(B)