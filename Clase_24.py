"""Clase 24     16-06-25"""

#Class= Son como un  molde, que nos permite crear objetos.
#Objetos= Son instancias de una clase, que tienen atributos y métodos.

"""Ejercicio tipo prueba"""

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
    opc=int(input("¿Qué es lo que le gustaría hacer?\n1-. Comprar entradas\n2-. Consultar comprador\n3-. Cancelar compra\n 4-.Continuar ingresando ventas o Salir del sistema.\n"))
    if opc==1:
        print("Has escogido \"Comprar entrada\".")
        comp_entr()
    elif opc==2:
        print("Has escogido \"Consultar comprador\".")
        cons_entr()
    elif opc==3:
        print("Has escogido \"Cancelar compra\".")
        canc_comp()
    elif opc==4:
        print("Has escogido \"Continuar ingresando ventas o salir del menú. \".")
    else: 
        print("Oh no, algo ha salido mal, debes volver a escoger una opción.")
        inicio_prog()

def main_user(user):
    class persona:
        def __init__(self,nombre, tipo_entr, codigo):
            self.nombre = nombre
            self.tipo_entr = tipo_entr
            self.codigo = codigo

        user = []
    while True:
        try:
            nombre=input("Ingrese el nombre de usuario: ").lower().strip()
            if nombre in user:
                print("Usuario ya está creado, intente de nuevo.")
                continue
            else:
                print("El usuario ha sido creado.")
        except ValueError:
            print("Error, intentelo de nuevo")
            continue
        
        tipo_entr=input("¿Qué tipo de entrada quiere?(General o VIP): ").strip().lower()
        if tipo_entr not in ["general", "vip"]:
            print("Tipo de entrada no válida. Debe escoger entre el \"General\" o \"VIP\".")
            continue
        elif tipo_entr == "general":
            print("El costo de la entrada general es de 10.000.")
        elif tipo_entr == "vip":
            print("El costo de la entrada VIP es de 50.000.")
        codigo=input("Ingrese el codigo de confirmación: ").strip()
        if len(codigo) < 6 or " " in codigo and any(c.isdigit() for c in codigo):
            print("El código de confirmación debe tener al menos 6 caracteres y no puede contener espacios.")
def comp_entr():
    print("Para poder comprar una entrada tienes que ingresar:\n- Nombre del comprador\n-Tipo de entrada (General o VIP)\n-Ingresar codigo de confirmación.")

    

def cons_entr():
    print("Para consultar su entrada tiene que buscar su nombre de usuario.")
    n

def canc_comp():
    print("Para cancelar la compra necesita ingresar su nombre de usuario")

def cont_salir():
    print("GEI")

def volver():
    print("")
inicio_prog()
