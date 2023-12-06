mensaje_cifrado=input("ingresa lo que queres descifrar")
desplazamiento = 3
mensaje =input("ingresa elmsje")
desplazamiento = 3
for i in range (len(cad)):
 cad = cad [i]

cad = chr(ord(c)+desp)%ord("Z")

def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            num = ord(letra)
            num += desplazamiento
            if letra.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif letra.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26
            mensaje_cifrado += chr(num)
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado
                 
def descifrar_cesar(mensaje, desplazamiento):
    return cifrar_cesar(mensaje, -desplazamiento)

mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
print(mensaje_descifrado)


mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print(mensaje_cifrado)



