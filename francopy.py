import random
print ("que dificultad quiere? 1_facil o 2_dificil")
x3= (int(input()))
if (x3==1):
    secreto=random.randint(1,20)
    intm=3
intr=0    
x=0
if (x3==2):
    secreto=random.randint(1,200)
    intm=7
while (intr < intm):
    intr=intr+1
    x=int(input("ingrese un numero"))
    if (secreto == x):
        print("el numero es igual al numero secreto")
        break
    if (secreto > x):
      print("el numero secreto es mayor al numero ingresado")
    else:
        print("el numero secreto es menor al numero ingresado")
