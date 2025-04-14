class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El número ingresado debe ser positivo."):
        super().__init__(mensaje)

def ingrese_numero(): # puede fallar
    palabra = input("ingrese un numero positivo: ")
    numero = int(palabra) # puede fallar
    if numero < 0:
        raise NumeroDebeSerPositivo()
    return numero

def main():
    while True:
        try:
            numero = ingrese_numero() # puede fallar
            numero2 = ingrese_numero() # puede fallar
            print(numero / numero2) # puede fallar
        except ValueError as e:
            print("le dije que ingrese un numero, burro")
        except ZeroDivisionError as e:
            print("No se puede dividir por cero")
        except NumeroDebeSerPositivo as e:
            print("el numero tiene que ser positivo")

if __name__ == '__main__':
    main()