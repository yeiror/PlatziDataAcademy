def areaTriangulo(base,altura):
    area=(base*altura)/2
    print("el área del triángulo es:",end=" ")
    return area

def esTriangulo(lado1,lado2,base):
    if(lado1+lado2>base and lado1+base>lado2 and lado2+base>lado1):
        print("Es un triángulo válido")
        return True
    else:
        print("No se puede hacer un triángulo con estas dimensiones")
        return None

def tipoTriangulo(lado1,lado2,base):
    if(lado1==lado2==base):
        print("Es un triángulo equilátero")
    elif (lado1!=lado2!=base):
        print("Es un triángulo escaleno")
    else:
        print("Es un triángulo isósceles")

def run():

    while True:
        menu=int(input("""Bienvenido/da al programa del reto Python Cardio de Platzi
        Este es el menú principal, seleccione una opción para ingresar a un ejercicio planteado
        
        1: Área de un triángulo
        2: Piedra, papel o tijera
        3: Conversor de millas a kilómetros
        4: Calculadora de volúmenes
        5: Rangos cambiantes
        0: para salir 
        """))
        if menu==1:
            print("Has escogido el programa para calcular el área de un triángulo")
            base=float(input("Ingresa la base del triángulo: "))
            altura=float(input("Ingresa la altura del triángulo: "))
            print(areaTriangulo(base,altura))
            print("Bonus track \n Ahora para saber el tipo de triángulo por favor introduce los 2 lados restantes (recuerda que la base es uno de sus lados)")
            lado1=float(input("Introduce el primer lado "))
            lado2=float(input("Introduce el segundo lado "))
            if(esTriangulo(lado1,lado2,base)):
                print(tipoTriangulo(lado1,lado2,base))
            

        elif menu==2:
            pass
        elif menu==3:
            pass
        elif menu==4:
            pass
        elif menu==5:
            pass
        elif menu==0:
            print("Has escogido terminar el programa, Bye")
            return False
        else:
            print("Has escogido una opción incorrecta...\n Vuelve a intentarlo")

if __name__=="__main__":
    run()