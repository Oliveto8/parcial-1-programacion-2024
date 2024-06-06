
def menu()->str:
  #limpiar_pantalla()
  print(f"{'\n--Menu de opciones--\n'}")
  print("1- Cargar archivo .CSV")
  print("2- Imprimir lista")
  print("3- Asignar rating")
  print("4- Asignar género")
  print("5- Filtrar por género")
  print("6- Ordenar películas")
  print("7- Informar Mejor Rating")
  print("8- Guardar películas .JSON")
  print("9- Salir")
  return input(f"\ningrese una opcion: ")

def pausar():
  import os
  print("")
  os.system("pause")

def limpiar_pantalla():
  import os
  os.system("cls")

def pedir_confirmacion(mensaje:str)->bool:
  rta = input(mensaje).lower()
  return rta == 'si'

