# 6 Práctica 
Sentencias condicionales. (6 puntos)

## Ejercicio 1 (1.5 puntos)
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.

Menú de recomendaciones
1. Literatura
2. Cine
3. Música
4. Videojuegos
5. Salir

### Al ingresar una opcion
opcion 1:

Lecturas recomendables:

* Esperándolo a Tito y otros cuentos de fútbol (Eduardo
Sacheri)
* El juego de Ender (Orson Scott Card)
* El sueño de los héroes (Adolfo Bioy Casares)

opcion 2:

Películas recomendables:

* Matrix (1999)
* El último samuray (2003)
* Cars (2006)

opcion  3:

Discos recomendables:

* Despedazado por mil partes (La Renga, 1996)
* Búfalo (La Mississippi, 2008)
* Gaia (Mago de Oz, 2003)

opcion 4:

* Videojuegos clásicos recomendables
* Día del tentáculo (LucasArts, 1993)
* Terminal Velocity (Terminal Reality/3D Realms, 1995)
* Death Rally (Remedy/Apogee, 1996)

opcion  5:

Gracias, vuelva prontos

Opción no válida, en caso de ingresar un número fuera de las opciones

  while True:
    opcion=int(input('''
    Escoje la opcion que mas te guste
    1.Literatura 
    2.Cine 
    3.Música 
    4.Videojuegos 
    5.Salir '''  )) 

    if(opcion == 1):
     print(f'''
     Lecturas recomendables:
     Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)
     El juego de Ender (Orson Scott Card)
     El sueño de los héroes (Adolfo Bioy Casares)
    ''')

    elif(opcion == 2):
     print(f'''
     Películas recomendables:
     Matrix (1999)
     El último samuray (2003)
     Cars (2006)
     ''')

    elif(opcion == 3):
     print(f'''
     Discos recomendables:
     Despedazado por mil partes (La Renga, 1996)
      Búfalo (La Mississippi, 2008)
     Gaia (Mago de Oz, 2003)
     ''')

    elif(opcion == 4):
     print(f'''
     Videojuegos clásicos recomendables
     Día del tentáculo (LucasArts, 1993)
     Terminal Velocity (Terminal Reality/3D Realms, 1995)
     Death Rally (Remedy/Apogee, 1996)
     ''')

    elif(opcion == 5):
     print(f'Gracias, vuelva prontos')
     break

    else:
     print(f'Opción no valida ')
    

## Ejercicio 2 (1.5 puntos)
Se pide por teclado un número y nos imprime los números primos que hay previos a este número.

Ejemplo: si ingresamos el 10 nos imprima del 1 a ese 10 cuales números son primos.

    inspeccion=True 
    while inspeccion:

      Num=int(input("Ingrese un numero: "))

      if Num > 0:
        print("Lo hiciste bien")

        inspeccion=False

        for i in range(2,Num):
          aumento=2
          esprimo=True

          while esprimo and aumento < i:

            if i & aumento == 0:
              esprimo=False
            else: 
              aumento += 1
          if esprimo:
            print(i,"Es primo")


      else:
        print("El numero ingresado no es correcto intentelo de nuevo")



## Ejercicio 3 (1.5 puntos)
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de lo que pagó
después de los 20 meses.

Al finalizar los 20 meses pago en total:

primer mes pago 10, segundo mes pago 20, tercer mes pago 30, cuarto mes pago 40, etc.

    Mensualidad = 10
    Total = 0

    Plaso=int(input("Ingrese el perido de meses"))

    for i in range(Plaso):
      print("El pago recomendad " + str(i+1) + " es: " + str(Mensualidad))
      Total += Mensualidad
      Mensualidad *=2

    print("El pago total es de: " + str(Total))
