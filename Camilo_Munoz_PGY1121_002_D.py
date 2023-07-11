
import numpy as np
import os

matriz = np.empty((10, 4), dtype=object)
p = 1

for i in range(10):
    for j in range(4):
        matriz[i, j] = p
        p += 1
ruts = []
recaudado = 0
def mostrar_deptos():
    for i in range(10):
        for j in range(4):
            print(matriz[i, j], end='       ')
        print()

def comprar_deptos():
    global matriz, ruts, recaudado
    mostrar_deptos()
    while(True):
        try:
            tipo_depto = input("Seleccione el tipo de departamento A (3.800 UF) | B (3.000 UF) | C (2.800 UF)| D (3.500 UF): ").lower()
            if tipo_depto == "a":
                    costo = 3800
                    break
            elif tipo_depto == "b":
                    costo = 3000
                    break
            elif tipo_depto == "c":
                    costo = 2800
                    break
            elif tipo_depto == "d":
                    costo = 3500
                    break
            else:
                print("Tipo de departamento incorrecto")
                return
                
        except ValueError:
            print("Error de digitación")
    #else:
        #print("El Tipo de departamento sleccionado.")
        #return

    while(True):
        try:
            num_depto= int(input("Seleccione el número de departamento: "))
            if num_depto < 1 or num_depto > 40:
                print("Número de departamento inválido.")
                return
            else:
                break
        except ValueError:
            print("Error de digitación, intente nuevamente!")

    fila = (num_depto - 1) // 4
    columna = (num_depto - 1) % 4
    if matriz[fila, columna] == "X":
        print("El departamento seleccionado no está disponible.")
        return
    while(True):
        try:
            rut = int(input("Ingrese el rut del cliente (sin guión): "))
            if(rut>9999999):
                ruts.append(rut)
                break
            else:
                print("El rut del cliente debe ser mayor a siete digitos")
        except ValueError:
            print("Error, debe ser un número y debe ser entero ")
    
    matriz[fila, columna] = "X"
    recaudado += costo
    print("DEPARTAMENTO COMPRADO EXITOSAMENTE!")
    os.system("pause")

def mostrar_recaudado():
    global recaudado
    print("Total recaudado:" + str(recaudado) + " UF")
    os.system("pause")

def mostrar_ruts():
    if len(ruts) == 0:
        print("No hay clientes registrados.")
    else:
        print("Listado de clientes:")
        for rut in sorted(ruts):
            print("- Rut:", rut)
    os.system("pause")

while (True):
    try:
        print(" | MENÚ DE CASA FELIZ |")  
        print(" ----------------------")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = int(input("Elija Opción: "))

        if opcion ==1:
            comprar_deptos()  
        elif opcion ==2:
            mostrar_deptos() 
        elif opcion ==3:
            mostrar_ruts()
        elif opcion ==4:
            mostrar_recaudado()
        elif opcion ==5:
            print("Gracias por utilizar la aplicación, Camilo Muñoz Parra 11/07/2023")
            break
    except ValueError:
        print("Opción incorrecta! seleccione una opción valida entre el 1 y 5.")



