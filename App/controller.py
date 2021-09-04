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
    sortArtistas(catalog)


def loadArte(catalog):
    """
    Carga los archivos de las obras de arte y se agrega a la lista de obras de arte
    """
    Artefile = cf.data_dir + 'Moma/Artworks-utf8-30pct.csv'
    input_file = csv.DictReader(open(Artefile, encoding='utf-8'))
    for arte in input_file:
        model.addobraarte(catalog, arte)


def loadArtista(catalog):
    """
    Carga los archivos de loas artistas y se agrega a la lista de autores
    """
    Artistafile = cf.data_dir + 'Moma/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistafile, encoding='utf-8'))
    for tag in input_file:
        model.addartista(catalog, tag)

# Funciones de ordenamiento


def sortArtistas(catalog):
    """
    Ordena los artistas por nacimiento
    """
    model.sortArtistas(catalog)

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
