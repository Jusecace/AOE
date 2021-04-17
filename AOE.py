
#while True:
while True:
    try:
        Comida = int(input ("Ingrese la cantidad de comida :"))
        break
    except ValueError:
        print('Ooops! Esto no parece una cantidad valida de comida. Vuelva a intentar con valores numericos. (ejemplo: 1,2,3...)')

print('Cantidad ingresada de comida:',Comida)

while True:
    try:
        Aldeanos = int(input("Ingrese la cantidad de aldeanos :"))
        break
    except ValueError:
        print('Ooops! Eso no es un valor valido de aldeanos. Intente de nuevo con valores numericos. (ejemplo: 1,2,3...)')

print('Cantidad ingresada de aldeanos:',Aldeanos)


def PasarDeEdadEnAOE2DE(Comida,Aldeanos):
    """Esta funcion permite saber si pasamos bien de Edad o no.
    La funcion muestra que se pasa de Edad cuando hay minimo 500 de comida y entre 21 y 25 aldeanos
    """
    
    if (Comida >= 500) and (Aldeanos >= 21) :
        print('Es el momento de pasar de edad')
    elif (Comida < 500) or (Aldeanos < 21) :
        if (Comida < 500) :
            print('Necesita mas comida, a seguir produciendo granjas o a cazar venaditos.')
        if (Aldeanos < 21 ) :
            print('Nop, a seguir produciendo aldeanos.')
        if (Comida < 500) and (Aldeanos > 25) :
            print('Muchos Aldeanos. Deje de producir Aldeanos y solo recoja comida.')
            
            
PasarDeEdadEnAOE2DE(Comida,Aldeanos)
    

