"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras de arte y artistas

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArte(catalog)
    loadArtista(catalog)
    sortArsortañostistas(catalog)

def loadArte(catalog):
    """
    Carga los archivos de las obras de arte y se agrega a la lista de obras de arte
    """
    Artefile = cf.data_dir + 'Moma/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(Artefile, encoding='utf-8'))
    for arte in input_file:
        model.addobraarte(catalog, arte)

def loadArtista(catalog):
    """
    Carga los archivos de loas artistas y se agrega a la lista de autores
    """
    Artistafile = cf.data_dir + 'Moma/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(Artistafile, encoding='utf-8'))
    for tag in input_file:
        model.addartista(catalog, tag)

# Funciones de ordenamiento

def sortArsortañostistas(catalog):
    """
    Ordena los artistas por nacimiento
    """
    model.sortArtistas(catalog)

def sortcostos(catalog):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.sortcostos(catalog)
    return orden

def sortBooks(catalog, size, ordenamiento):
    """
    Ordena los libros por average_rating
    """
    return model.sortBooks(catalog, size, ordenamiento)

def sortobras(catalog):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.sortobras(catalog)
    return orden
    
# Funciones de consulta sobre el catálogo

def obtener_ultimos_artes(catalog):
    """
    Retorna los tres ultimas obras de arte cargadas
    """
    ultimostres = model.obtener_ultimos_artes(catalog)
    return ultimostres

def obtener_ultimos_artistas(catalog):
    """
    Retorna los tres ultimos artistas cargados
    """
    ultimostresartistas = model.obtener_ultimos_artistas(catalog)
    return ultimostresartistas

def nacidos_rango(catalog, año_inicial, año_final):

    nacidos_rango = model.nacidos_rango(catalog,año_inicial,año_final)
    return nacidos_rango

def comprados_rango(catalog, fecha_inicial, fecha_final):

    nacidos_rango = model.comprados_rango(catalog,fecha_inicial,fecha_final)
    return nacidos_rango

def obtener_ultimos_nacidos(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    ultimostresartistas = model.obtener_ultimos_nacidos(catalog)
    return ultimostresartistas

def obtener_primeros_nacidos(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    primerostresartistas = model.obtener_primeros_nacidos(catalog)
    return primerostresartistas

def consulta_codigo(catalog,codigo):
    artista = model.consulta_codigo(catalog,codigo)
    return artista

def filtrar_depto(catalog,departamento):
    obras = model.filtrar_depto(catalog,departamento)
    return obras

def cantidad_tecnicas(catalog):
    tecnicas = model.cantidad_tecnicas(catalog)
    return tecnicas

def consulta_obras(catalog,tecnica):
    obras = model.consulta_obras(catalog,tecnica)
    return obras

def calculo_de_transporte(catalog):
    """
    Ordena los artistas por nacimiento
    """
    obras = model.calculo_de_transporte(catalog)
    return obras

def suma_costo(catalog):
    """
    Ordena los artistas por nacimiento
    """
    costo = model.suma_costo(catalog)
    return costo

def suma_peso(catalog):
    """
    Ordena los artistas por nacimiento
    """
    peso = model.suma_peso(catalog)
    return peso

def obtener_costosas(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    costosas = model.obtener_costosas(catalog)
    return costosas

def buscar_artistas(codigos,catalog):
    nombres = model.buscar_artistas(codigos,catalog)
    return nombres

def obtener_antiguas(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    orden = model.obtener_antiguas(catalog)
    return orden

def obras_rango(catalog, año_inicial, año_final):

    obras_rango = model.obras_rango(catalog,año_inicial,año_final)
    return obras_rango

def obtener_ultimas_obras(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    obtener_ultimas_obras = model.obtener_ultimas_obras(catalog)
    return obtener_ultimas_obras

def obtener_primeras_obras(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    obtener_primeras_obras = model.obtener_primeras_obras(catalog)
    return obtener_primeras_obras

def obtener_compradas(catalog):
    """
    Retorna los tres ultimos artistas nacidos
    """
    obtener_compradas = model.obtener_compradas(catalog)
    return obtener_compradas