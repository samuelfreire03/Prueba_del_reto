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
    catalog['artista'] = lt.newList('ARRAY_LIST')
    catalog['Referencias_Autor_ObradeArte'] = lt.newList('ARRAY_LIST',cmpfunction=compareauthors)

    return catalog

# Funciones para agregar informacion al catalogo

def addobraarte(catalog, arte):

    lt.addLast(catalog['obra_de_arte'], arte)

    authors = arte['ConstituentID'].replace("[","").replace("]","").split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addreferncias(catalog, author.strip(), arte)


def addartista(catalog, arte):
    lt.addLast(catalog['artista'], arte)

def addreferncias(catalog,artista, arte):

    authors = catalog['Referencias_Autor_ObradeArte']
    posauthor = lt.isPresent(authors, artista)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = nuevoSubcatalogArtistas(artista)
        lt.addLast(authors, author)
    lt.addLast(author['obras'], arte)

# Funciones para creacion de datos

def nuevoSubcatalogArtistas(arte):

    referecnias = {'artista': "", "obras": None}
    referecnias['artista'] = arte
    referecnias['obras'] = lt.newList('ARRAY_LIST')
    return referecnias

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

# Funciones utilizadas para comparar elementos dentro de una lista

def compareauthors(authorname1, author):
    if (authorname1.lower() in author['artista'].lower()):
        return 0
    return -1

# Funciones de ordenamiento