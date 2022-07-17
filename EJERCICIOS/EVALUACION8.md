# Práctica 8. (6 puntos)
## Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un
diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
valores sean los cuadrados de las claves.

Ejemplo: si se ingresa el 4 imprima el cuadrado de 1, de 2, de 3 y de 4

    inspeccion=True 
    while inspeccion:
      Num1=int(input("Ingrese un numero: " ))

      if Num1 > 0:
        i=1
        while i>Num1:
          creciente=1
          espositivo=True

          while creciente < i:
            if i & creciente == 0:
              espositivo=False
            else:
              creciente += 1

      else:
        print("El numero ingresado no es correcto intentelo de nuevo")

## Ejercicio 2 (2 puntos)
Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada carácter en la cadena.

Ejemplo: si se ingresa "paloma" p=1 a=2 l=1 o=1 m=1

    cadena=input('Ingrese texto')
    print(cadena)
    list=[]
    diccionario={}
    for each in cadena:
      list.append(each)
    list.sort()
    try:
        while(lista[0]):
            cuenta=(list.count(lista[0]))
            caracter=list[0]
            diccionario[caracter]=cuenta
            for x in range(cuenta):
              list.pop(0)
            if(len(list)==0):
              break
    except:
        print('Error !')
    print(diccionario)

## Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta
y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de
los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras
cada consulta el programa nos preguntará si queremos hacer otra consulta.

    FrutPrecios = {
        "mango" : 20.5,
        "manzana" : 50.2,
        "pera" : 30,
        "uva" : 40.5,
        "sandía" : 20,
        "fresa" : 60.5,
        "platano" : 16.5,
        "melón" : 35.5,  
        "limon" : 50,
    }
    
    realizarConsulta = True
    while realizarConsulta:
        print('Consulta de Precios')
        fruta = input('Qué fruta esta buscando?')
        if fruta in FrutPrecios:
            print(f'El precio de la {fruta} es de ${FrutPrecios[fruta]} por kilo.')
            kilos = input('Cuántos kilos?')
            try:
                costo = FrutPrecios[fruta] * float(kilos)
                print(f'El precio final es de ${costo}')
            except:
                print('Error')        
        else:
            print(f'Error, {fruta} no existe')
        print('Quiere realizaer otra consulta')
        consulta = input('''Precione s si desea continuar''')
        if consulta == 's':
            realizarConsulta = True
        else:
            realizarConsulta = False
    print('Gracias vuelva pronto ;)')
