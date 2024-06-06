from funciones_menu import *
from funciones import *

"""Enunciado:
Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
id_peli, titulo, genero, rating
por ejemplo: 1,Adventures of Rocky,sin genero,0
2,My Brother the Devil,sin genero,0
3,Criminal,sin genero,0
Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
nuevos archivos de salida de formato similar filtrados por varios criterios:
el programa contará con el siguiente menú:
1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de
diccionarios los elementos del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
calculado de manera aleatoria se mostrará por pantalla el mismo.
4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
1: drama
2: comedia
3: acción
4: terror
5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
donde solo aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
9) Salir."""

seguir = "si"
archvivo_cargado = False
archvio_con_rating = False
archivo_full = False

while seguir == "si":
  match menu():
    case "1":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      print("\nArchvio cargado correctamente")
      archvivo_cargado = True
    case "2":
      if archvivo_cargado:
        imprimir_lista(lista_peliculas)
      else:
        print("\nAntes de imprimir la lista primero tenemos que cargar el archivo")
    case "3":
      if archvivo_cargado:
        lista_con_rating = asignar_rating_aleatorio(lista_peliculas)
        imprimir_lista(lista_con_rating)
        archvio_con_rating = True
      else:
        print("\nAntes de imprimir la lista primero tenemos que cargar el archivo")
    case "4":
      if archvio_con_rating:
        lista_con_rating_y_genero = asignar_genero_aleatorio(lista_con_rating)
        imprimir_lista(lista_con_rating_y_genero)
        archivo_full = True
      else:
        print("\nAntes de imprimir la lista primero tenemos que cargar el archivo y tener el rating cargado")

    case "5":
      if archivo_full:
        print("\nOpciones de género:")
        print("-drama")
        print("-comedia")
        print("-acción")
        print("-terror")
        genero_seleccionado = input("\nIngrese el género deseado: ")
        peliculas_filtradas = filtrar_por_genero(lista_con_rating_y_genero, genero_seleccionado)

        if peliculas_filtradas:
          nombre_archivo_nuevo = f"{genero_seleccionado}.csv"
          escribir_archivo_csv(peliculas_filtradas, nombre_archivo_nuevo)
          print(f"\nSe guardaron las peliculas del genero '{genero_seleccionado}' en el archivo: '{nombre_archivo_nuevo}'.")
        else:
            print(f"\nNo se encontraron peliculas del genero '{genero_seleccionado}'.")
      else:
        print("\nAntes de filtrar por genero, primero debemos tener la lista con genero cargado")

    case "6":
      if archivo_full:
        mostrar_peliculas_por_genero(lista_con_rating_y_genero)
      else:
        print("\nAntes de filtrar por genero, primero debemos tener la lista con genero cargado")
    case "7":
      pass
    case "8":
      pass
    case "9":
      if pedir_confirmacion("\n¿Confirmar salida? "):
        seguir = "no"
        continue
    case _:
      print("\nIngrese uno de los numneros indicados")
  pausar()

print("\nFin del programa")