"""Clase 24     16-06-25"""

#Class= Son como un  molde, que nos permite crear objetos.
#Objetos= Son instancias de una clase, que tienen atributos y métodos.

"""Ejercicio tipo prueba"""
"""haga un programa que permita generar un menu de ingreso de usuario.

el programa debe:

1. tener un menu principal, que muestre 4 opciones:

  1. Ingresar usuario

  2. buscar usuario

  3. eliminar usuario

  4. salir

2. al ingresar la opcion 1:

  -se debe solicitar el nombre del usuario, sexo, clave. (por separado)

  -para que el ingreso del usuario sea exitoso, se debe compartir lo siguiente:

    *el nombre del usuario no estar repetido

    *el sexo del usuario debe ser definido como 'M' o 'F'

    *la contraseña debe ser de un minimo de 8 caracteres, al menos un numero, una letra y no contener espacios.

  -en caso de que el ingreso del usuario sea exitoso, se debe mostrar un mensaje de confirmacion.

3. al ingresar la opcion 2:

  -se debe solicitar el nombre del usuario a buscar.

  -si el usuario existe, se debe mostrar su informacion (nombre, sexo, clave).

  -si no existe, se debe mostrar un mensaje de error.

4. al ingresar la opcion 3:

  -se debe solicitar el nombre del usuario a eliminar.

  -si el usuario existe, se debe eliminar y mostrar un mensaje de confirmacion.

  -si no existe, se debe mostrar un mensaje de error.

5. al ingresar la opcion 4:

  -se debe mostrar un mensaje de despedida y salir del programa.

6. en caso de ingrear una opcion no valida, se debe mostrar un mensaje de error y volver al menu principal.



todas las opciones deben estar definidas en funciones separadas e incluidas en una función main."""

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Persona:

  def __init__(self, nombre, clave, sexo):

    self.nombre = nombre

    self.clave = clave

    self.sexo = sexo



def menu_principal():

  print("Menu Principal:")

  print("1. Ingresar usuario")

  print("2. Buscar usuario")

  print("3. Eliminar usuario")

  print("4. Salir")

  return input("Seleccione una opcion (1-4): ")



def ingresar_usuario(usuarios):

  while True:

    nombre = input("Ingrese el nombre del usuario: ").strip().lower()

    if nombre in usuarios:

      print("El nombre de usuario ya existe. Intente con otro.")

      continue

    break

  while True:

    sexo = input("Ingrese el sexo del usuario (M/F): ").upper()

    if sexo not in ['M', 'F']:

      print("Entrada invalida. Intente de nuevo.")

      continue

    break

  while True:

    clave = input("Ingrese la clave del usuario (minimo 8 caracteres, al menos un numero y una letra): ")

    if len(clave) < 8 or not any(c.isdigit() for c in clave) or not any(c.isalpha() for c in clave):

      print("Entrada invalida. Intente de nuevo.")

      continue

    break

  usuarios[nombre] = Persona(nombre, clave, sexo)

  print("Usuario ingresado exitosamente.")

  return usuarios



def buscar_usuario(usuarios):

  nombre = input("Ingrese el nombre del usuario a buscar: ").strip().lower()

  if nombre in usuarios:

    usuario = usuarios[nombre]

    print(f"Usuario encontrado: Nombre: {usuario.nombre}, Sexo: {usuario.sexo}, Clave: {usuario.clave}")

  else:

    print("Usuario no encontrado.")



def eliminar_usuario(usuarios):

  nombre = input("Ingrese el nombre del usuario a eliminar: ").strip().lower()

  if nombre in usuarios:

    del usuarios[nombre]

    print(f"Usuario {nombre} eliminado exitosamente.")

  else:

    print("Usuario no encontrado.")



def main():

  usuarios = {}

  while True:

    opcion = menu_principal()

    if opcion == "1":

      usuarios = ingresar_usuario(usuarios)

    elif opcion == "2":

      buscar_usuario(usuarios)

    elif opcion == "3":

      eliminar_usuario(usuarios)

    elif opcion == "4":

      print("¡Hasta luego!")

      break

    else:

      print("Opcion invalida. Intente de nuevo.")



main()
