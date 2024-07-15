#presentar los primeros 50 numeros de la sucesion de fibonacci, usando bucle for y range
N1=0
N2=1
C=0
for C in range(50):
    print(N1)
    S=N1+N2
    N1=N2
    N2=S
    C=C+1
    
    