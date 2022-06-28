## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.

    Dato1 = input('Ingrese la cantidad de grados Fahrenheit')
    resultado = int(Dato1) - 32 *  5/9
    print(str(Dato1 + ' F, son ' + str(resultado) + 'c')) 

2.2 Ejercicio 2 (1.5 puntos)

Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.

    num = 0
    num1 = 0

    num = input('ingresa un numero ')
    num1 = input ('ingresa otro numero ')

    opsum = int(num) + int(num1) 
    oprest =  int(num) - int(num1)
    opdiv = int(num) / int(num1)
    opmult = int(num) * int(num1)

    print('Los resutados son' , str(opsum) + ' de la suma ' + str(oprest) + ' de la resta ' + str(opdiv) + ' de la divicion ' + str(opmult) + ' de la multiplicacion ')

2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

    L=0
    B=0
    A=0

    L= input('ingrese  la medida del lado ')
    B= input('Ingrese la medida de la base ')
    A= input('Ingrese la medida de la altura ')

    peri = int(L) * int(L)
    area = int(B) * int(A) / 2

    print('El perimetro es de ' + str(peri))
    print('El area es de ' + str(area))

