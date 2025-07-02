# Menú de gestión de inscripciones para una maratón:

# Crea un programa en Python que permita gestionar las inscripciones para una maratón. El menú debe tener las siguientes opciones (cada una implementada en una función):

#1-. Inscribir corredor:

#   Solicita el nombre del corredor (no debe repetirse).
#   Solicita la categoría (5K, 10K o 21K).
#   Cada categoría tiene un máximo de 30 cupos.
#   Ingresar un código de inscripción (mínimo 5 caracteres, debe tener al menos una letra y un número, sin espacios).
#   Si cumple todo, registra la inscripción como exitosa.

# 2-. Consultar corredor:

#    Permite buscar un corredor por nombre.
#   Si existe, muestra nombre, categoría y código.
#   Si no existe, muestra "Corredor no inscrito".

# 3-. Eliminar inscripción:

#   Permite eliminar un corredor por nombre.
#   Si no existe, muestra "Corredor no inscrito".

# 4-. Mostrar total de inscritos por categoría.

# 5-. Salir del sistema.

# Todas las opciones deben estar implementadas en funciones separadas y el menú debe estar en la función principal.

class persona:
    def __init__(self, nombre,categoria,codigo):
        self.nombre=nombre
        self.categoria=categoria
        self.codigo=codigo

usuarios={}
maraton={"5k":30,"10k":30,"21k":30}

def bienvenida():
    print("Bienvenido al menú de la maratón.")
    main()


def inscribir():
    print("Para poder inscribirte necesitas:\nIngresar tu nombre.\nEscoger la maratón en la que participararás.\nIngresar un codigo de verificación.")
    while True:
        user=input("Ingrese nombre del corredor: ").strip().lower()
        if user in usuarios:
            print("El usuario ingresado ya existe, intentelo de nuevo.")
            continue
        elif user not in usuarios:
            print(f"Usuario ingresado exitosamente, hola {user}")

        mar= input("Maratones en la que puedes participar:\n 5K\n 10K\n 21K\n Ingrese el monto exacto(Ej: 5k): ").strip().lower().replace(" ","")
        if mar in ("5k","10k","21k") and maraton[mar] >0:
            print(f"Has seleccionado la maratón {mar}")
            usuarios[user] = mar
            maraton[mar] -=1
        elif maraton[mar] <=0:
            print("No hay stock en este momento")
            return
        else:
            print("Error, intentelo de nuevo.")
            continue
    
        while True:
            code=input("Ingrese codigo de verificación: ").strip()
            if len(code) != 5:
                print("Codigo incorrecto, tiene que ser de 5 caracteristicas.")
                continue
            elif " " in code:
                print("Codigo incorrecto, no puede tener espacio.")
                continue
            elif not any(c.isalpha() for c in code):
                print("Codigo incorrecto, le falta letra.")
                continue
            elif not any(c.isupper() for c in code):
                print("Codigo incorrecto, tiene que tener al menos una mayuscula.")
                continue
            elif not any(c.islower() for c in code):
                print("Codigo incorrecto, tiene que tener al menos una minuscula")
                continue
            elif not any(c.isdigit() for c in code):
                print("Codigo incorrecto, falta al menos un numero en el codigo.")
                continue
            else:
                print("Codigo correcto.")
                usuarios[user]= persona(user,mar,code)
                maraton[mar]-=1
                return

def consultar(usuarios):
    while True:
        nombre= input("Para consultar corredor ingrese su nombre: ").strip().lower()
        if nombre in usuarios:
            corredor= usuarios[nombre]
            print(f"Nombre: {corredor.nombre}")
            print(f"Maraton: {corredor.categoria}")
            print(f"Codigo: {corredor.codigo}")
            break
        elif nombre not in usuarios:
            op=input("¿Quiere seguir consultando corredores?").lower().replace("í","i")
            if op== "si":
                continue
            elif op =="no":
                break
            else:
                print("Por favor ingrese \"Sí\" o \"No\"")
        else:
            print("Corredor no inscrito.")
            continue

def eliminar():
    while True:
        nombre =input("Ingrese el usuario que quiere eliminar.")
        if nombre not in usuarios:
            print("El usuario seleccionado no existe.")
            break
        elif nombre in usuarios:
            del usuarios[nombre]
            print("Usuario borrado exitosamente.")
            break
        else:
            print("Ha habido un error, intentolo de nuevo")
            continue

def categorias():
        print("Total de inscritos por categoría: ")
        print(f" Los inscritos en la maraton 5k= {30 - maraton['5k']}")
        print(f" Los inscritos en la maraton 10k= {30 - maraton['10k']}")
        print(f" Los inscritos en la maraton 21k= {30 - maraton['21k']}")
    
def main():
    while True:
        try:
            opc=int(input("1-. Inscribir corredor\n2-. Consultar corredor\n3-. Eliminar inscripción\n4-. Mostrar total de inscritos por categoria\n5-. Salir del programa\nSeleccione su opción: "))

            if opc== 1:
                inscribir()
            elif opc==2:
                consultar(usuarios)
            elif opc ==3:
                eliminar()
            elif opc ==4:
                categorias()
            elif opc== 5:
                print("Adios, vuelve pronto")
                break
        except ValueError:
            print("Error, ha ingresado una respuesta no valida, intentelo de nuevo.")
            return
bienvenida()
