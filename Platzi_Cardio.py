import os
import math
import random

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
            
        elif menu==3:
            borrarPantalla()
            while(True):
                print("""Bienvenido al conversor de Millas a Km 
                Escoge una opción en pantalla:
                1- Convertir de Km a Millas
                2- Convertir de Millas a Km 
                0- Para salir""")
                opcion=int(input())
                if(opcion==1):
                    km=float(input("Ingrese la cantidad de Km que desea convertir: "))
                    print(km, " kilómetros equivalen a ", km/1.609344, " millas")
                   
                elif(opcion==2):
                    millas=float(input("Ingrese la cantidad de millas que desea convertir: "))
                    print(millas, " millas equivalen a ", millas*1.609344, " kilómetros")
                    
                elif(opcion==0):
                    print("Muchas gracias por usar el conversor Bye")
                    break
                else:
                    print("Has ingresado una opción incorrecta Vuelve a ingresar ")
                
        elif menu==4:
            borrarPantalla()
            while(True):
                print("""Bienvenido a la calculadora de Volúmenes 
                Escoge una opción en pantalla:
                1- Volúmen de un cilindro
                2- Volúmen de la esfera 
                0- Para salir""")
                opcion=int(input())
                if(opcion==1):
                    radio=float(input("Ingresa el radio de la base del cilindro en cm "))
                    h=float(input("Ingresa la altura del cilindro en cm "))
                    print("El volumen del cilindro es", round(math.pi*radio*radio*h,2))
                   
                elif(opcion==2):
                    radio=float(input("Ingresa el radio de la esfera cilindro en cm "))
                    print("El volumen del cilindro es", round((4/3)*math.pi*radio*radio*radio,2))
                    
                elif(opcion==0):
                    print("Muchas gracias por usar la calculadora de volúmenes, Bye")
                    break
                else:
                    print("Has ingresado una opción incorrecta Vuelve a ingresar ")
       
        elif menu==5:
            print("Bienvenido al juego de rangos cambiantes")
            lim_final=random.randint(0,101)
            lim_init=random.randint(0,lim_final+1)
            while True:
                valor=int(input("ingresa un valor entre 0 y 100 para saber si está en el rango"))
                if(lim_init<=valor<=lim_final):
                    print("El número está en el rango ", lim_init," - " ,lim_final )
                    break
                elif(lim_final<valor):
                    print("Te pasaste, sigue intentando") 
                    
                elif(lim_init>valor):
                    print("Estas por debajo del rango")

        elif menu==0:
            print("Has escogido terminar el programa, Bye")
            return False
        else:
            print("Has escogido una opción incorrecta...\n Vuelve a intentarlo")

if __name__=="__main__":
    run()