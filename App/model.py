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

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from datetime import date
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
    catalog = {'obra_de_arte': None,'artista': None,'nacidos_primero': None,'obras_ordenadas': None, 'obras_a_llevar':None}

    catalog['obra_de_arte'] = lt.newList('ARRAY_LIST')
    catalog['artista'] = lt.newList('ARRAY_LIST')
    catalog['nacidos_primero'] = lt.newList('ARRAY_LIST')
    catalog['obras_ordenadas'] = lt.newList('ARRAY_LIST',cmpfunction=comparecodigos)
    catalog['obras_a_llevar'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addobraarte(catalog, arte):
    lt.addLast(catalog['obra_de_arte'], arte)
    lt.addLast(catalog['obras_a_llevar'], arte)

    artistas = arte['ConstituentID'].replace("[","")
    artistas = artistas.replace("]","")
    artistas = artistas.split(",")

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

def newCosto(codigo_obra,costo,peso,titulo,artistas,clasificacion,fecha,dimensiones,tecnica):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artista = {'codigo': "", "costo": None, "peso": None}
    artista['codigo'] = codigo_obra
    artista['costo'] = costo
    artista['peso'] = peso
    artista['titulo'] = titulo
    artista['artistas'] = artistas
    artista['clasificacion'] = clasificacion
    artista['fecha'] = fecha
    artista['dimensiones'] = dimensiones
    artista['tecnica'] = tecnica
    return artista

def newTecnica(nombre_tecnica):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    tecnica = {'Tecnica': "", "Cantidad": 0}
    tecnica['Tecnica'] = nombre_tecnica
    tecnica['Cantidad'] = None
    return tecnica
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

def consulta_codigo(catalog,nombre):

    artistas = catalog['artista']
    obras = catalog['obras_ordenadas']
    for artista in lt.iterator(artistas):
        if nombre.lower().strip() in artista['DisplayName'].lower().strip():
            codigo = artista['ConstituentID']

    for artista in lt.iterator(obras):
        if codigo == artista['codigo'].replace("]","").replace("[",""):
            artista_final = artista
    return artista_final

def cantidad_tecnicas(artistas):

    cantidad_de_tecnicas_veces = lt.newList('ARRAY_LIST',cmpfunction=comparetecnicas)
    tecnicas_final = lt.newList('ARRAY_LIST')
    for partes in lt.iterator(artistas['obras']):
        lt.addLast(tecnicas_final,partes['Medium'])

    for i in lt.iterator(tecnicas_final):
        posauthor = lt.isPresent(cantidad_de_tecnicas_veces, i)
        if posauthor > 0:
            artista = lt.getElement(cantidad_de_tecnicas_veces, posauthor)
            artista['Cantidad'] += 1
        else:
            artista = newTecnica(i)
            artista['Cantidad'] = 1
            lt.addLast(cantidad_de_tecnicas_veces, artista)
        
    k = 0
    for p in lt.iterator(cantidad_de_tecnicas_veces):
        if int(p['Cantidad']) > k:
            k = p['Cantidad']
            maximo = p['Tecnica']
    
    return maximo,cantidad_de_tecnicas_veces

def consulta_obras(artistas,tecnica):

    obras = lt.newList('')
    for obra in lt.iterator(artistas['obras']):
        if obra['Medium'] == tecnica:
            lt.addLast(obras,obra)

    return obras

def filtrar_depto(catalog, departamento):

    obras = lt.newList()
    for p in lt.iterator(catalog['obras_a_llevar']):
        if p['Department'].lower() == departamento.lower():
            lt.addLast(obras, p)

    return obras

def calculo_de_transporte(catalog):

    obras = lt.newList('ARRAY_LIST')
    for obra in lt.iterator(catalog):

        peso = obra['Weight (kg)'] 
        altura = obra['Height (cm)'] 
        ancho = obra['Width (cm)'] 
        profundidad = obra['Depth (cm)']
        longitud = obra['Length (cm)']
        diametro = obra['Diameter (cm)']

        if (altura == 0 or altura == '') and (ancho == 0 or ancho == ''):
            costo = 48.00

        elif (longitud != 0 and longitud != '') and (ancho != 0 and ancho != '') and (altura == 0 or altura == ''):
            costo = (float(longitud)*float(ancho)*72)/10000 

        elif (altura != 0 and altura != '') and (ancho != 0 and ancho != ''):
            costo = (float(altura)*float(ancho)*72)/10000
            if (profundidad != 0 and profundidad != ''):
                costo = max((float(altura)*float(ancho)*72)/10000,(float(altura)*float(ancho)*72*float(profundidad))/10000)
            if (peso != 0 and peso != '') and (profundidad != 0 and profundidad != ''):
                costo = max((float(peso) * 72)/10000,(float(altura)*float(ancho)*72)/10000,(float(altura)*float(ancho)*72*float(profundidad))/10000)
            elif (peso != 0 and peso != '') and (profundidad == 0 or profundidad == ''):
                costo = max((float(peso) * 72)/10000,(float(altura)*float(ancho)*72)/10000)
        elif (peso != 0 and peso != ''):
            costo1 = (float(peso) * 72)/10000
            costo = max(costo1,costo)

        if (diametro != 0 and diametro != '') and (altura != 0 and altura != ''):
            costo = ((float(diametro)**2)*float(altura)*72*3.14)/10000 
            
        if (peso == 0 or peso == ''):
            pesar = 0
        else: 
            pesar = peso 
        precio = newCosto(obra['ObjectID'],costo,pesar,obra['Title'],obra['ConstituentID'],obra['Classification'],obra['Date'],obra['Dimensions'],obra['Medium'])

        if precio['costo'] == 0:
            precio['costo'] = 48.00
        lt.addLast(obras,precio)
    return obras

def suma_costo(catalog):

    suma = 0
    for p in lt.iterator(catalog):
        suma += p['costo']

    return float(suma)

def suma_peso(catalog):

    suma = 0
    for p in lt.iterator(catalog):
        suma += float(p['peso'])

    return float(suma)

def obtener_costosas(catalog):
    """
    Retorna los tres ultimos artistas cargados
    """
    costosas = lt.newList()
    for cont in range(1, 6):
        arte = lt.getElement(catalog, cont)
        lt.addLast(costosas, arte)
    return costosas

def buscar_artistas(codigos,catalog):

    nombres = lt.newList('ARRAY_LIST')
    nuevos_codigos = codigos.replace("[","")
    nuevos_codigos = nuevos_codigos.replace("]","")
    nuevos_codigos = nuevos_codigos.split(",")

    artistas = catalog['artista']
    for codigo in nuevos_codigos:
        for p in lt.iterator(artistas):
            if codigo == p['ConstituentID']:
                lt.addLast(nombres,p['DisplayName'])
    return nombres

def obtener_antiguas(catalog):
    """
    Retorna los tres ultimos artistas cargados
    """
    ordenadas = sortantiguas(catalog)
    con_fecha = lt.newList()
    orden = lt.newList()
    for obra in lt.iterator(ordenadas):
        if obra['fecha'] != '':
            lt.addLast(con_fecha, obra)
    for cont in range(1, 6):
        arte = lt.getElement(con_fecha, cont)
        lt.addLast(orden, arte)
    return orden

# Funciones utilizadas para comparar elementos dentro de una lista

def compareaños(artista1, artista2):
    return (float(artista1['BeginDate']) < float(artista2['BeginDate']))

def compareantiguas(artista1, artista2):
    return ((artista1['fecha']) < (artista2['fecha']))

def comparacostos(artista1, artista2):
    return (float(artista1['costo']) > float(artista2['costo']))

def comparecodigos(codigo1, codigo):
    if (codigo1.lower() == codigo['codigo'].lower()):
        return 0
    return -1

def comparetecnicas(tecnica1, tecnica):
    if (tecnica1.lower() == tecnica['Tecnica'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2):

    if artwork1['DateAcquired'] == '':

        fecha1 = 0
    else: 
        fecha1 = int((date.fromisoformat(artwork1['DateAcquired'])).strftime("%Y%m%d%H%M%S"))

    if artwork2['DateAcquired'] == '':

        fecha2 = 0

    else:
        fecha2 = int((date.fromisoformat(artwork2['DateAcquired'])).strftime("%Y%m%d%H%M%S"))

    return fecha1 < fecha2

# Funciones de ordenamiento

def sortArtistas(catalog):
    sa.sort(catalog['nacidos_primero'], compareaños)

def sortcostos(catalog):
    orden = sa.sort(catalog, comparacostos)
    return orden

def sortantiguas(catalog):
    orden = sa.sort(catalog, compareantiguas)
    return orden

def sortBooks(catalog, size, ordenamiento):

    sub_list = lt.subList(catalog['obra_de_arte'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if ordenamiento == 'Insertion':
        sorted_list = insertion.sort(sub_list, cmpArtworkByDateAcquired)
    elif ordenamiento == 'Shell':
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif ordenamiento == 'Merge':
        sorted_list = merge.sort(sub_list, cmpArtworkByDateAcquired)
    elif ordenamiento == 'Quick':
        sorted_list = quick.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,sorted_list
