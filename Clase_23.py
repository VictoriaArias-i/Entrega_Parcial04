""" Clase 23      13-06-25"""

#   Temario Prueba 27-06-25:

#               - Lista y Diccionario.
#               - Funciones, simples y return
#               - While, try y except.
#               - Script e Input.

"""Repaso:"""

# Lista: Almacenamiento de datos que mantiene un orden, mantienen elementos multiplicados. Es un conjunto ordenado.
# Diccionario: Almacenamiento de datos, es más complcado pero se puede borrar info con comandos, es mutable. Es un conjuto desordenado.0
# Funciones: 

#   Realicen un programa en Python, que permita generar un menú de gestión de entradas para el concierto de Noche de brujas.
# Menú principal:
#   - Comprar entradas: Se debe permitir ingresar el nombre del comprador, tipo de entrada y codigo de confirmación por separado. 
#   - Consultar comprador: Debe permitir buscar compradores mediante el nombre. Si el comprador existe debería mostrar datos asociados. Si no existe el usuario debe salir "Comprador no existe"
# Si existe el usuario te muestra el nombre del comprador, tipo de entrada y codigo de confirmación por separado. 
#   - Cancelar compra: El menú debe permitir o mostrar una opcion que permita eliminar un comprador con toda su información asociada a dicho comprador.
#   - Continuar ingresar ventas o Salir del sistema.
# Todas las opciones tiene que estar implementas mediantes funciones separadas del codigo principal (MAIN).
# Para que la compra sea exitosa se tiene que cumplir con esto:
    #a) El nombre del comprador no debe repetirse.
    #b) La entrada general tiene un costo de 10.000 y el VIP 50.000
    #c) El codigo de confirmación tiene que tener un minimo de 6 caracteres, con uno o más numeros y sin espacios, con mayuscual y minuscula.
    #d) En el caso de cumplir con todas las condiciones la compra se resgitra como exitosa.

print("Bienvenido al menú para comprar una entrada al concierto de \"Noche de brujas\".")

def inicio_prog():
    while True:
        try:
            opc=int(input("¿Qué es lo que le gustaría hacer?\n1-. Comprar entradas\n2-. Consultar comprador\n3-. Cancelar compra\n4-.Continuar ingresando ventas o Salir del sistema.\n"))
            if opc==1:
                print("Has escogido \"Comprar entrada\".")
                comp_entra()
            elif opc==2:
                print("Has escogido \"Consultar comprador\".")
                cons_entr()
            elif opc==3:
                print("Has escogido \"Cancelar compra\".")
                cance_comp()
            elif opc==4:
                print("Has escogido \"Continuar ingresando ventas o salir del menú. \".")
            else: 
                print("Oh no, algo ha salido mal, debes volver a escoger una opción.")
                inicio_prog()
        except ValueError:
            print("Error, el numero ingresado es del 1 al 4.")
compradores= []
class persona:
    def __init__(self,nombre, tipo_entr, codigo):
        self.nombre = nombre
        self.tipo_entr = tipo_entr
        self.codigo = codigo

def comp_entra():
    global compradores
    compradores = compradores
    while True:
        try:
            nombre=input("Ingrese el nombre de usuario: ").lower().strip()
            if any(comprador.nombre == nombre for comprador in compradores):
                print("Usuario ya está creado, intente de nuevo.")
                continue
            else:
                tipo_entr = input("¿Qué tipo de entrada quiere? (General o VIP):").strip().lower()
                if tipo_entr not in ["general", "vip"]:
                    print("Tipo de entrada no valida, debe escoger entre \"General\" o \"Vip\".")
                    continue
                elif tipo_entr == "general":
                    print("El costo de la entrada general es de 10.000.")
                elif tipo_entr == "vip":
                    print("El costo de la entrada VIP es de 50.000.")

            codigo=input("Ingrese el codigo de confirmación: ").strip()
            if len(codigo) < 6 or " " in codigo and any(c.isdigit() for c in codigo):
                print("El código de confirmación debe tener al menos 6 caracteres y no puede contener espacios.")
                continue
            if not any(c.isdigit() for c in codigo) or not any(c.isupper() for c in codigo) or not any(c.islower() for c in codigo):
                print("El código de confirmación debe contener al menos un número, una mayúscula y una minúscula.")
                continue
            if any(comprador.codigo == codigo for comprador in compradores):
                print("El código de confirmación ya está en uso, intente con otro.")
                continue
            
            compradores.append(persona(nombre, tipo_entr, codigo))
            print(f"Compra exitosa para {nombre} con tipo de entrada {tipo_entr} y código {codigo}.")
            break
        except ValueError:
            print("Error, intentelo de nuevo")
            continue

def cons_entr():
    """Función para consultar comprador."""
    global compradores
    nombre = input("Ingrese el nombre de usuario para consultar: ").lower().strip()
    comprador = next((c for c in compradores if c.nombre == nombre), None)
    if comprador:
        print(f"Nombre: {comprador.nombre}")
        print(f"Tipo de entrada: {comprador.tipo_entrada}")
        print(f"Código de confirmación: {comprador.codigo}")
    else:
        print("Comprador no existe.")
def cance_comp():
    """Función para cancelar compra."""
    global compradores
    nombre = input("Ingrese el nombre de usuario para cancelar la compra: ").lower().strip()
    comprador = next((c for c in compradores if c.nombre == nombre), None)
    if comprador:
        compradores.remove(comprador)
        print("Compra cancelada exitosamente.")
    else:
        print("Comprador no existe.")

def cont_salir():
    """Función para continuar o salir del sistema."""
    while True:
        opcion = input("¿Desea continuar ingresando ventas o salir del sistema? (continuar/salir): ").strip().lower()
        if opcion == "continuar":
            print("Regresando al menú principal...")
            return
        elif opcion == "salir":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida, intente de nuevo.")
            cont_salir()
inicio_prog()
