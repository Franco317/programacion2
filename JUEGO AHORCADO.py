import random		
IMÁGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
frutas='manzana pera sandia kiwi mango lechuga'.split()
quintillizas= 'nino_nakano yotsuba_nakano ichika_nakano'.split()
def jugarDeNuevo():
    print('le gustaria jugar?')
    rta=input().lower()
    if (rta.startwith('s')):
        return True
    else:
        return False

Ejecutar=True
while (Ejecutar):
    print(obtenerPalabra(LDP))
    ejecutar = jugarDeNuevo()

def obtenerPalabra(LDP):
    x=random.randint(0, len(palabras)-1)
    palabraSecreta=LDP[x]
    return palabraSecretaprint(obtenerPalabra(quintillizas))
