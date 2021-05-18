import os

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

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
    elif (lado1!=lado2 and lado1!=base and lado2!=base):
        print("Es un triángulo escaleno")
    else:
        print("Es un triángulo isósceles")

def PiedraPapelTijeras(jugador1:str,jugador2:str):
    if jugador1==jugador2:
        print("Empate")
        return None
    if((jugador1=="piedra" and jugador2=="tijeras")or(jugador1=="papel" and jugador2=="piedra")or(jugador1=="tijeras" and jugador2=="papel")):
        print("Gana Jugador 1 con ",jugador1)
        return True
    elif((jugador2=="piedra" and jugador1=="tijeras")or(jugador2=="papel" and jugador1=="piedra")or(jugador2=="tijeras" and jugador1=="papel")):
        print("Gana Jugador 2 con ", jugador2)
        return False

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
            borrarPantalla()
            print("Has escogido el programa para calcular el área de un triángulo")
            base=float(input("Ingresa la base del triángulo: "))
            altura=float(input("Ingresa la altura del triángulo: "))
            print(areaTriangulo(base,altura))
            print("\nBonus track\n Ahora para saber el tipo de triángulo \npor favor introduce los 2 lados restantes (recuerda que la base es uno de sus lados)")
            lado1=float(input("Introduce el primer lado "))
            lado2=float(input("Introduce el segundo lado "))
            if(esTriangulo(lado1,lado2,base)):
                tipoTriangulo(lado1,lado2,base)
                     
            
        elif menu==2:
            borrarPantalla()
            print("Has escogido el juego piedra, papel o tijeras")
            i=0
            puntaje_j1,puntaje_j2=0,0
            while i<3:
                print("Ronda N° ", i+1)
                jugador1=input("Jugador 1, escriba una de las siguientes opciones \n piedra\n papel\n tijeras ")
                jugador2=input("Jugador 2, escoja una de las siguientes opciones \n piedra\n papel\n tijeras ")
                borrarPantalla()
                if((jugador1=="piedra" or jugador1=="papel" or jugador1=="tijeras")and (jugador2=="piedra" or jugador2=="papel" or jugador2=="tijeras")):
                    bandera=PiedraPapelTijeras(jugador1,jugador2)
                    if (bandera==True):
                        puntaje_j1+=1
                        i+=1
                    elif(bandera==False):
                        puntaje_j2+=1
                        i+=1
                else:
                    print("Ingresaste una opción inválida")
                
                print("El puntaje es el siguiente \n Jugador 1: ", puntaje_j1, "\n Jugador 2: ", puntaje_j2, "\n")
            
            if(puntaje_j1>puntaje_j2):
                print("El jugador 1 es el ganador\n")
            else:
                print("El jugador 2 es el ganador\n")
                


                    
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