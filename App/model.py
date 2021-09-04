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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de Obras de arte. Para Crea en primer lugar dos entradas cada una para autores y obras de artes
    y luego para cada una de estas crea una lista  vacia, donde se guarda la informacion.
    """
    catalog = {'obra_de_arte': None,'artista': None,'Referencias_Autor_ObradeArte': None}

    catalog['obra_de_arte'] = lt.newList()
    catalog['artista'] = lt.newList()
    catalog['nacidos_primero'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addobraarte(catalog, arte):
    lt.addLast(catalog['obra_de_arte'], arte)

def addartista(catalog, arte):
    lt.addLast(catalog['artista'], arte)
    lt.addLast(catalog['nacidos_primero'], arte)

# Funciones para creacion de datos

# Funciones de consulta

def obtener_ultimos_artes(catalog):
    """
    Retorna los tres ultimas obras de arte cargadas
    """
    artes = catalog['obra_de_arte']
    ultimostres = lt.newList()
    for cont in range(lt.size(artes)-2, lt.size(artes)+1):
        arte = lt.getElement(artes, cont)
        lt.addLast(ultimostres, arte)
    return ultimostres

def obtener_ultimos_artistas(catalog):
    """
    Retorna los tres ultimos artistas cargados
    """
    artes = catalog['artista']
    ultimostres = lt.newList()
    for cont in range(lt.size(artes)-2, lt.size(artes)+1):
        arte = lt.getElement(artes, cont)
        lt.addLast(ultimostres, arte)
    return ultimostres

def nacidos_rango(catalog, año_inicial, año_final):

    artistas = catalog['nacidos_primero']
    booknacidos_rango = lt.newList()
    for artista in lt.iterator(artistas):
        if año_inicial <= int(artista['BeginDate']) and año_final >= int(artista['BeginDate']):
            lt.addLast(booknacidos_rango,artista)
    return booknacidos_rango

def obtener_ultimos_nacidos(catalog):
    """
    Retorna los tres  ultimos artistas nacidos
    """
    ultimostres = lt.newList()
    for cont in range(lt.size(catalog)-2, lt.size(catalog)+1):
        arte = lt.getElement(catalog, cont)
        lt.addLast(ultimostres, arte)
    return ultimostres

def obtener_primeros_nacidos(catalog):
    """
    Retorna los tres  primeros artistas nacidos
    """

    primeros_tres = lt.newList()
    for cont in range(1, 4):
        arte = lt.getElement(catalog, cont)
        lt.addLast(primeros_tres, arte)
    return primeros_tres

# Funciones utilizadas para comparar elementos dentro de una lista

def compareratings(artista1, artista2):
    return (float(artista1['BeginDate']) < float(artista2['BeginDate']))

# Funciones de ordenamiento

def sortArtistas(catalog):
    sa.sort(catalog['nacidos_primero'], compareratings)
