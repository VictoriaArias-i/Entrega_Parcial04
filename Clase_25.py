"""Clase 25     18-06-25"""

"""Programar un menú de gestión de entradas para un concierto de GitHub con movimiento original, con su diferente show. el menú principal debe permitir 4 opciones.
opciones:
1) Venta de entradas.
2) Cambio de show.
3) Mostrar stock de funciones.
4) salir del programa.
Todas las opciones del menú deben estar implementadas mediante funciones.
Al ingresar a la opción número 1:
 -solicitar el nombre del usuario
 -seleccionar el show 
 *ambas por separado.
 para que la solicitud sea exitosa, se deben cumplir los siguientes requerimientos:
 -Nombre del comprador (no debe repetirse).
 -la selección del show debe permitir seleccionar entradas para 1 de las dos funciones.
  ~Movimiento original + tripulación.
  ~Movimiento original + sonrisa.
 -debe haber un máximo de 50 entradas para cada función.
 -En caso de cumplir con todas los requerimientos, registrar entrada como exitosa.
Al ingresar la opción número 2:
 -El menú debe permitir cambiar el show seleccionado.
Al ingresar la opción número 3:
 -Mostrar el total de entradas disponibles para cada una de las funciones.
Al ingresar la opción número 4:
 -salir del programa
En caso de elegir una opción valida, solicitar al usuario volver a ingresar una opción permitida."""


compradores= {}
stock={"Movimiento original + tripulación": 50, "Movimiento original + sonrisa": 50}

def bienvenida():
    print("Bienvenido al menú de compra.")
    main()

def main():
    
    while True:
        try:
            print("1-. Venta de entrada.\n2-. Cambio de show.\n3-. Mostrar stock de funciones.\n4-. Salir del programa.")
            opc= int(input("Escoja una opción: "))
            if opc == 1:
                venta(compradores, stock)
            elif opc==2:
                cambio_show(compradores, stock)
            elif opc==3:
                mostrar_stock(compradores, stock)
            elif opc==4:
                print("Adios, vuelve pronto.")
                break       
            else:
                print("Algo ha salido mal, intentelo de nuevo, ha escogido un numero no valido.")
                continue
        except ValueError:
            print("No ha ingresado una respuesta valida, intentelo de nuevo.")
            continue

def venta(compradores, stock):
        user=input("Nombre de usuario: ").strip().lower()
        if user in compradores:
            print("El usuario ya ha sido ingresado, intentelo de nuevo.")
            return    
        show=int(input("Seleccione un show:\n1-. Movimiento original + tripulación\n2-. Movimiento original + sonrisa\n"))
        if show in (1,2) and stock[show] >0:
            compradores[user] = show
            stock[show] -=1
            print("Compra exitosa.")
        elif show not in (1,2):
            print("No ha ingresado el show indicado.")
        elif stock[stock] == 50:
            print("No quedan entradas")
        else:
            print("Error, intentelo de nuevo.")
            return

def cambio_show(compradores, stock):
    nombre = input("Ingrese su nombre para cambiar de show: ").strip().lower()
    if nombre not in compradores:
        print("No hay compra registrada a este nombre.")
        return
    elif nombre in compradores:
        show_actual = compradores[nombre]
        otro_show= 2 if show_actual ==1 else 1
        if stock[otro_show] >0:
            compradores[nombre]= otro_show
            stock[show_actual] +=1
            stock[otro_show] -=1
            print(f"Show cambiado exitosamente de {show_actual} a {otro_show}")
        else:
            print("No hay entradas disponibles para el otro show.")

def mostrar_stock(compradores, stock):
    print("Entradas disponibles por función: ")
    print(f"1-. Movimiento orginal + tripulación {stock['Movimiento orginal + tripulación']}")
    print(f"1-. Movimiento orginal + sonrisa {stock['Movimiento orginal + sonrisa']}")    

bienvenida()
