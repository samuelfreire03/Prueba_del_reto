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


from DISClib.DataStructures.arraylist import newList
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
    catalog = {'obra_de_arte': None,'artista': None,'nacidos_primero': None,'obras_ordenadas': None}

    catalog['obra_de_arte'] = lt.newList()
    catalog['artista'] = lt.newList()
    catalog['nacidos_primero'] = lt.newList()
    catalog['obras_ordenadas'] = lt.newList('ARRAY_LIST',cmpfunction=compareartistas)

    return catalog

# Funciones para agregar informacion al catalogo

def addobraarte(catalog, arte):
    lt.addLast(catalog['obra_de_arte'], arte)

    artistas = arte['ConstituentID'].replace("[","").replace("]","").split(",")

    for artista in artistas:
        addinfoartista(catalog, artista.strip(), arte)

def addartista(catalog, arte):
    lt.addLast(catalog['artista'], arte)
    lt.addLast(catalog['nacidos_primero'], arte)

def addinfoartista(catalog, codigo_artista, arte):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    artistas = catalog['obras_ordenadas']
    posauthor = lt.isPresent(artistas, codigo_artista)
    if posauthor > 0:
        artista = lt.getElement(artistas, posauthor)
    else:
        artista = newArtista(codigo_artista)
        lt.addLast(artistas, artista)
    lt.addLast(artista['obras'], arte)

# Funciones para creacion de datos

def newArtista(codigo_artista):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artista = {'codigo': "", "obras": None}
    artista['codigo'] = codigo_artista
    artista['obras'] = lt.newList('ARRAY_LIST')
    return artista

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

def consulta_codigo(catalog,codigo):

    artistas = catalog['artista']
    obras = catalog['obras_ordenadas']
    for artista in lt.iterator(artistas):
        if codigo.lower().strip() in artista['DisplayName'].lower().strip():
            nombre = artista['ConstituentID']

    for artista in lt.iterator(obras):
        if nombre == artista['codigo']:
            artista_final = artista

    return artista_final

def cantidad_tecnicas(artistas):

    cantidad_de_tecnicas_veces = {}
    tecnicas_final = lt.newList('ARRAY_LIST')
    for partes in lt.iterator(artistas['obras']):
        lt.addLast(tecnicas_final,partes['Medium'])

    for i in lt.iterator(tecnicas_final):
        if i in cantidad_de_tecnicas_veces:
            cantidad_de_tecnicas_veces[i] += 1
        else: 
            cantidad_de_tecnicas_veces[i] = 1

    k = 0
    for p in cantidad_de_tecnicas_veces:
        if cantidad_de_tecnicas_veces[p] > k:
            k = cantidad_de_tecnicas_veces[p]
            maximo = p
    
    return maximo

def consulta_obras(artistas,tecnica):

    obras = lt.newList('')
    for obra in lt.iterator(artistas['obras']):
        if obra['Medium'] == tecnica:
            lt.addLast(obras,obra)

    return obras


# Funciones utilizadas para comparar elementos dentro de una lista

def compareratings(artista1, artista2):
    return (float(artista1['BeginDate']) < float(artista2['BeginDate']))

def compareartistas(authorname1, author):
    if (authorname1.lower() in author['codigo'].lower()):
        return 0
    return -1

# Funciones de ordenamiento

def sortArtistas(catalog):
    sa.sort(catalog['nacidos_primero'], compareratings)
