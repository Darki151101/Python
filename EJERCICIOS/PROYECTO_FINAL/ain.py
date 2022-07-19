"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
# se importan las biblioteca random  para obtene las plabras aleatorias
import random
# se importa la biblioteca string para que random procese palabras
import string
# este comando nos permite mandar a llamar a el arcvio con las palablar designdas
from palabras import palabras
# este comando nos permite mandar a llamar a el arcvio con el diccionario (vidas_diccionario_visual)
from ahorcado_diagramas import vidas_diccionario_visual

# se declara la funcion para validar las palabras 
def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras) 

# Este bucle nos permite repetir el prceso y almasenar las palbras
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

# se declara la funcion para mostrar el mensaje el inicio del juego y designar el numero de vidas conforme al diccionaro (vidas_diccionario_visual) creado anterior mente 
def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase) 
    letras_adivinadas = set()  

    vidas = 7

# se fabrica el bucle  para re petir el proceso conforme al numero de vidas ya preestablecida
    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper()
# se delcra un if para designar las letras de las palabras escojidas por random en caso de escribir la palbar correcta se gana 
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
# se declara este segundo if para notificar el numero de lteras restantes
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
# de equivocarse  este else lo notificara              
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
# de escojer la misma letra este elif te notifacara        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
# de meter una carater no relacionada a letras este else te mostra un mensaje de eror             
        else:
            print("\nEsta letra no es válida.")

# si agotas tus vidas este if se encargara de notifcarlo   
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
# y si lo logras pues este else te dira que lo logratse       
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado()
