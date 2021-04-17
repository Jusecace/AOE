#!/usr/bin/python

import sys 

while True:
    try :
        comida   = input("Ingrese la cantidad de Comida:") 
        aldeanos = input("Ingrese la cantidad de Aldeanos:") 
        # Evaluamos si los datos ingresados son enteros <int> y si son mayores a 0.
        if ( int(comida) > 0 ) and  ( int(aldeanos) > 0 ) :
            print('Cant. Comida: {}, Cant. Aldeanos: {}').format(comida, aldeanos)
            break
        else :
            print('Se deben usar numeros enteros <int> positivos')
    except IndexError:
        print('Hay que ejecutar el programa con dos parametros') 
    except ValueError: 
        print(' Los dos parametros deben ser numeros enteros <int> mayores a cero (0)')
    
def PasarDeEdadEnAOE2DE(comida,aldeanos):
    """Esta funcion permite saber si pasamos bien de Edad o no.
    La funcion muestra que se pasa de Edad cuando hay minimo 500 de comida y entre 21 y 25 aldeanos
    """
    
    if (comida >= 500) and (aldeanos >= 21) :
        print('Es el momento de pasar de edad')
    elif (comida < 500) or (aldeanos < 21) :
        if (comida < 500) :
            print('Necesita mas comida, a seguir produciendo granjas o a cazar venaditos.')
        if (aldeanos < 21 ) :
            print('Nop, a seguir produciendo aldeanos.')
        if (comida < 500) and (aldeanos > 25) :
            print('Muchos aldeanos. Deje de producir aldeanos y solo recoja comida.')
            
            
PasarDeEdadEnAOE2DE(comida,aldeanos)
    

