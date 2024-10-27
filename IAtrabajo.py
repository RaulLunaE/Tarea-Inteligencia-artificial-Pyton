#Tareas
#centrar palabras
def centrar(cad):
    ancho_pantalla = 80
    longitud_cad = len(cad)
    espacio_izquierdo = (ancho_pantalla - longitud_cad) // 2
    print(' ' * espacio_izquierdo + cad)

#multiplo
def EsMultiplo(a, b):
    return a % b == 0

#temperatura
def calcularTemperaturaMedia(temp1, temp2):
    return (temp1 + temp2) / 2

#orden
def Intercambiar(a, b):
    return (max(a, b), min(a, b))

#conversor de tiempo
def Convertir_A_Segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

#conversor de tiempo 2.0 
def Convertir_A_HMS(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = segundos % 60
    return horas, minutos, seg
#inicio de mi menu
def menu():
    while True:
        print("\n                      "+"Menú:")
        print("\n1. Centrar una cadena")
        print("2. Verificar si un número es múltiplo de otro")
        print("3. Calcular temperatura media")
        print("4. Intercambiar dos números")
        print("5. Convertir horas, minutos y segundos a total de segundos")
        print("6. Convertir segundos a horas, minutos y segundos")
        print("7. Salir\n\n")
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == '1':
            cadena = input("\n\nIngrese la cadena a centrar: ")
            centrar(cadena)
        
        elif opcion == '2':
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            if EsMultiplo(num1, num2):
                print(f"{num1} es múltiplo de {num2}.")
            else:
                print(f"{num1} no es múltiplo de {num2}.")
        
        elif opcion == '3':
            temp1 = float(input("Ingrese la primera temperatura: "))
            temp2 = float(input("Ingrese la segunda temperatura: "))
            media = calcularTemperaturaMedia(temp1, temp2)
            print(f"\n\nLa temperatura media es: {media}°C")
        
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            mayor, menor = Intercambiar(num1, num2)
            print(f"\n\nNúmeros ordenados: {mayor}, {menor}")
        
        elif opcion == '5':
            while True:  # Bucle para repetir la entrada hasta que sea válida
                horas = int(input("Ingrese la cantidad de horas: "))
                minutos = int(input("Ingrese la cantidad de minutos (0-59): "))
                segundos = int(input("Ingrese la cantidad de segundos (0-59): "))
                
                # Validación de minutos y segundos
                if not (0 <= minutos < 60):
                    print("Error: Los minutos deben estar entre 0 y 59.")
                elif not (0 <= segundos < 60):
                    print("Error: Los segundos deben estar entre 0 y 59.")
                else:
                    total_segundos = Convertir_A_Segundos(horas, minutos, segundos)
                    print(f"\n\nTotal en segundos: {total_segundos}")
                    break  # Salir del bucle si la entrada es válida
        
        elif opcion == '6':
            segundos = int(input("Ingrese la cantidad de segundos: "))
            horas, minutos, seg = Convertir_A_HMS(segundos)
            print(f"\n\nCorrespondencia: {horas} horas, {minutos} minutos y {seg} segundos.")
        
        elif opcion == '7':
            print("\n\nSaliendo del programa...")
            break
        
        else:
            print("\n\nOpción no válida. Por favor, seleccione una opción del 1 al 7.")

#Esto es para controlar el programa solo sirve con phyton IAtranajo.py
if __name__ == "__main__":
    menu()
