import os
import csv
import random

nombre_archivo = "movies.csv"

def get_path_actual(nombre_archivo): #1
  directorio_actual = os.path.dirname(__file__)
  return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo_csv(nombre_archivo): #1
  ruta_archivo = get_path_actual(nombre_archivo)
  with open(get_path_actual(ruta_archivo), "r", encoding="utf-8") as archivo:
    lista = []
    encabezado = archivo.readline().strip("\n").split(",") #lo leo pero no lo muestro
    
    for linea in archivo.readlines():
      pelicula = {}
      linea = linea.strip("\n").split(",")
      id, titulo, genero, rating = linea 
      
      pelicula["id"] = int(id)
      pelicula["titulo"] = titulo
      pelicula["genero"] = genero    
      pelicula["rating"] = float(rating)

      lista.append(pelicula)
    return lista

def imprimir_lista(lista): #2
  print("ID  | Título                      | Género        | Rating")
  print("----|-----------------------------|---------------|-------")
  for pelicula in lista:
    id = int(pelicula["id"])
    titulo = pelicula["titulo"]
    genero = pelicula["genero"]
    rating = float(pelicula["rating"])
    print(f"{id:<3}  {titulo:<30} {genero:<12}   {rating:0.1f}")

def asignar_rating_aleatorio(lista): #3
  for pelicula in lista:
    rating = random.uniform(1, 10)
    pelicula["rating"] = rating
  return lista

def asignar_genero_aleatorio(lista): #4
  for pelicula in lista:
    num_aleatorio = random.randint(1, 4)
    if num_aleatorio == 1:
      pelicula["genero"] = "drama"
    elif num_aleatorio == 2:
      pelicula["genero"] = "comedia"
    elif num_aleatorio == 3:
      pelicula["genero"] = "acción"
    else:
      pelicula["genero"] = "terror"
  return lista

def filtrar_por_genero(lista, genero): #5
  peliculas_filtradas_genero = []
  for pelicula in lista:
    if pelicula["genero"] == genero:
      peliculas_filtradas_genero.append(pelicula)
  return peliculas_filtradas_genero

def escribir_archivo_csv(lista, nombre_archivo): #5
  ruta_archivo = os.path.join("pelicula_genero", nombre_archivo) #carpeta pelicula_genero
  with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("id,titulo,genero,rating\n")
    for pelicula in lista:
      archivo.write(f"{pelicula['id']},{pelicula['titulo']},{pelicula['genero']},{pelicula['rating']}\n")

def filtrar_peliculas_genero(lista: list): #6
  peliculas_por_genero = {}
  for pelicula in lista:
    genero = pelicula["genero"]
    peliculas = peliculas_por_genero.get(genero, [])
    peliculas.append(pelicula)
    peliculas_por_genero[genero] = peliculas
  return peliculas_por_genero

def mostrar_peliculas_por_genero(lista: list): #6
  peliculas_por_genero = filtrar_peliculas_genero(lista)
  for genero in peliculas_por_genero:
    peliculas = peliculas_por_genero[genero]
    total_peliculas = len(peliculas)
    for i in range(total_peliculas - 1):
      for j in range(0, total_peliculas - i - 1):
        if peliculas[j]["rating"] < peliculas[j + 1]["rating"]:
          peliculas[j], peliculas[j + 1] = peliculas[j + 1], peliculas[j]
    peliculas_por_genero[genero] = peliculas
  
  for genero in peliculas_por_genero:
    print(f"\nGénero: {genero}:\n")
    for pelicula in peliculas_por_genero[genero]:
      print(f"Título: {pelicula['titulo']}, Rating: {pelicula['rating']:0.1f}")
