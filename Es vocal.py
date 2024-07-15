#ingresar una letra y determinar si es vocal, validar que se ingrese un solo caracter
while True:
    C=input("Ingrese un caracter: ")
    if len(C)==1:
        break
    else:     
        print("Solo debe ingresar una letra")
V=["a","e","i","o","u","A","E","I","O","U"]
if C in V:
    print(f"{C} es una vocal")
else:
    print(f"{C} no es una vocal")