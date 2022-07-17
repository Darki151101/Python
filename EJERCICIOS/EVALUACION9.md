# Práctica 9. Programación funcional. (6 puntos)
## Ejercicio 1 (2 puntos)
Realice un programa que pregunte aleatoriamente una multiplicación. El programa
debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea
incorrecta el programa debe indicar cuál es la correcta). El programa preguntará
10 multiplicaciones, y al finalizar mostrará el número de aciertos.

#### Análisis
* Hacemos un bucle con 10 iteraciones, en cada iteración se inicializan dos
números con un valor aleatorio (de 2 a 10). Se calcula la multiplicación.
* Mostramos la multiplicación, y pedimos por teclado el resultado. Si
coincide con la multiplicación calculada cuento un acierto, sino escribimos un
mensaje de error mostrando el resultado correcto. Cuando salimos del bucle
mostramos el número de aciertos.

Ejemplo. imprime una multiplicacion (9 * 8 =  )por teclado se ingresa la respuesta, eso pasa 10 veces y al final nos imprime cuantas respuestas fueron correctas

Recuerda el import random

    import random
    aciert=0
    for i in range(0,10,1):
      num=random.randint(2,9)
      num1=random.randint(2,9)
      resul= num*num1
      res=input(f'{num}x{num1}=')
      res=int(res)
      if resul==res:
        aciert=aciert+1

## Ejercicio 2 (2 puntos)
Obtener el cuadrado de todos los elementos en la lista.

Lista: [1,2,3,4,5,6,7,8,9,10]

    def potcuad(num):
     return pow(num,2)

    list1=[1,2,3,4,5,6,7,8,9,10]

    list2= list(map(potcuad,list1))

    list2

## Ejercicio 3 (2 puntos)
Obtener la cantidad de elementos mayores a 5 en la tupla.

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

    def mayorqcinco(a):
      if (a>5):
        return True
      else:
        return False
    listtup=[55,2,6,7,8,10,77,55,2,1,30,4,2,3]
    Mayorcinco=list(filter(mayorqcinco,listtup))
    Mayorcinco

## Ejercicio 4 (2 puntos)
Obtener la suma de todos los elementos en la lista

lista = [1,2,3,4]

    from functools import reduce
    numis=[1,2,3,4]
    sum=reduce(lambda x, y: x + y,numis)
    print(sum)
