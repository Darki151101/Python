# Práctica 7. Programación orientada a objetos. (6 puntos)
## Ejercicio 1 (2 puntos)
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y
DNI. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.

● mostrar(): Muestra los datos de la persona.

● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

    class Persona:

      def __init__(self, nombre, edad,DNI):
        self.nombre=input("Introdusca su nombre")
        self.edad=int(input("Dijite su edad"))
        self.DNI=int(input("Intrudusca su DNI"))

        def Adulto(self):
          if self.edad>17:
            print(self.edad, "Es Adulto")
          else:
            print(self.edad, "Es Menor de edad puede ser una dolecente o un niño")

    persona1=Persona()
    persona1.Adulto()
     
   ![image](https://user-images.githubusercontent.com/99523872/179247073-753634d0-a224-4018-a856-a85411061eb2.png)

## Ejercicio 2 (2 puntos)
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
una persona) y cantidad (puede tener decimales). El titular será obligatorio y la
cantidad es opcional. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. El atributo no se puede
modificar directamente, sólo ingresando o retirando dinero.

● mostrar(): Muestra los datos de la cuenta.

● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.

● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar
en números rojos.

    class Cuenta():
      def __init__(self,titular,cantidad):
        self.titular = titular
        self.catidad = cantidad

        def mostrar(slef):
          print('La infomacion del cliente es: ')
          print(f'Titular de la cuneta {self.titular}')
          print(f'Saldo disponible {self,cantidad }')

    class cajAhorro(Cuenta):
      def __init__(self,cantidad):
        super.__init__(cantidad):

      def Info(self):
          print(f'Dispone actualmente {self.cantidad} en su cuenta de ahorro')

    class PlazoFijo(Cuenta):
        def __init__(self, cantidad, plazo, interes, importe):
            super().__init__(cantidad) 
            self.importe = importe                                                                                     
            self.interes = interes 
            self.plazo = plazo
        def importInteres(self):
            self.importe = self.cantidad * self.interes / 100
            print(f'El interes genrado por el imprte es de:{self.importe}')
            print(f'Generado durante: {self.plazo}')

    cliente1= cajAhorro('Carmen' 120000)
    cliente1.mostrar()



    cliente1 = PlazoFijo(120000, '5 Año', 6, 120000)
    cliente1.importInteres()
    
![image](https://user-images.githubusercontent.com/99523872/179247433-5e4082df-69bf-4eae-8ca7-cf090ac60208.png)


## Ejercicio 3 (2 puntos)
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará
expresada en tanto por ciento.Construye los siguientes métodos para la clase:

● Un constructor.

● Los setters y getters para el nuevo atributo.

● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad;, por lo tanto hay que crear un método es Titular Válido ( ) que
devuelve verdadero si el titular es mayor de edad pero menor de 25 años y
falso en caso contrario.

● Además la retirada de dinero sólo se podrá hacer si el titular es válido.

● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.

● Piensa los métodos heredados de la clase madre que hay que reescribir.

    class CuentaJoven():
      def __init__(self,titular,cantidad,edad):
        self.titular=input("Nombre del titular")
        self.catidad=int(intput("Cantidad a depositar"))
        self.edad=int(input("Su edad"))

      def mostrar(slef):
          print('La infomacion del cliente es: ')
          print(f'Titular de la cuneta {self.titular}')
          print(f'Cantidad depositada {self.cantidad }')
          print(f'Edad {self.edad}')

      def Adulto(self):
        if self.edad>17:
          print(self.nombre, "Es Adulto")
        else:
          print(self.nombre, "Es Menor de edad puede ser una dolecente o un niño")



    cliente1=CuentaJoven()
    cliente1.Adulto()

