compradores_show1 = []
compradores_show2 = []
MAX_ENTRADAS = 50

SHOWS = {
    1: "Movimientos originales con la tripulación",
    2: "Movimientos originales con sonrisa"
}

def ingresar_nombre_comprador():
    while True:
        nombre = input("Ingrese nombre del comprador: ").strip().title()
        if not nombre:
            print("Debe ingresar al menos un carácter válido.")
            continue
        if nombre in compradores_show1 or nombre in compradores_show2:
            print("Ese nombre ya tiene una entrada. Intente con otro.")
            continue
        return nombre

def seleccionar_show():
    while True:
        print("\nSeleccione función:")
        for num, desc in SHOWS.items():
            print(f" {num}. {desc}")
        try:
            op = int(input("Opción (1-2): ").strip())
            if op in SHOWS:
                return op
            else:
                print("Opción fuera de rango. Elija 1 o 2.")
        except ValueError:
            print("Ingrese un número válido (1 ó 2).")

def ventas_de_entradas():
    print("\n--- Venta de Entradas ---")
    nombre = ingresar_nombre_comprador()
    show = seleccionar_show()

    if show == 1:
        if len(compradores_show1) >= MAX_ENTRADAS:
            print("Lo siento, ya no quedan entradas para la función 1.")
            return
        compradores_show1.append(nombre)
    else:
        if len(compradores_show2) >= MAX_ENTRADAS:
            print("Lo siento, ya no quedan entradas para la función 2.")
            return
        compradores_show2.append(nombre)

    print(f"¡Compra exitosa! {nombre} tiene su entrada para '{SHOWS[show]}'.")

def cambio_de_show():
    print("\n--- Cambio de Show ---")
    nombre = input("Ingrese nombre del comprador a cambiar: ").strip().title()
    if nombre in compradores_show1:
        actual = 1
    elif nombre in compradores_show2:
        actual = 2
    else:
        print("Comprador no registrado.")
        return

    destino = seleccionar_show()
    if destino == actual:
        print("Ya estás registrado en esa misma función.")
        return

    if destino == 1 and len(compradores_show1) >= MAX_ENTRADAS:
        print("No hay cupos disponibles en la función 1.")
        return
    if destino == 2 and len(compradores_show2) >= MAX_ENTRADAS:
        print("No hay cupos disponibles en la función 2.")
        return

    if actual == 1:
        compradores_show1.remove(nombre)
        compradores_show2.append(nombre)
    else:
        compradores_show2.remove(nombre)
        compradores_show1.append(nombre)

    print(f"Cambio exitoso: {nombre} ahora está en '{SHOWS[destino]}'.")

def mostrar_stock_funciones():
    disponibles1 = MAX_ENTRADAS - len(compradores_show1)
    disponibles2 = MAX_ENTRADAS - len(compradores_show2)
    print("\n--- Stock de Funciones ---")
    print(f" Función 1 ({SHOWS[1]}) disponible: {disponibles1}")
    print(f" Función 2 ({SHOWS[2]}) disponible: {disponibles2}")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Ventas de entradas")
        print("2. Cambio de show")
        print("3. Mostrar stock funciones")
        print("4. Salir")
        op = input("Elija una opción (1-4): ").strip()
        if op == "1":
            ventas_de_entradas()
        elif op == "2":
            cambio_de_show()
        elif op == "3":
            mostrar_stock_funciones()
        elif op == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 4.")

menu_principal()
