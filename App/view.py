"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Mostrar los tres primeros y los tres ultimos artistas, segun el orden cronologico de un rango de años")
    print("3- Mostrar las tres primeras y las tres ultimas obras de arte, segun el orden cronologico de un rango de fechas")
    print("4- Clasificacion de obras por tecnica, y algunso datos sobre la tecnica mas usada de un artista dado")
    print("5- Clasificacion de obras segund su nacionalidad, y datos imprtantes sobre esta la nacionalidad mas repetida")
    print("6- Calculo del costo total de trasnporte de obras")
    print("7- Creacion de una nueva exposicion de arte")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo del museo
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los datos del mueso en la estructura de datos
    """
    controller.loadData(catalog)

def printobras_arte(elementos):
    size = lt.size(elementos)
    if size:
        print(' Estos son las ultimas tres obras de arte que se cargaron: ' + '\n')
        print(elementos['first']['info'],'\n')
        print(elementos['first']['next']['info'],'\n')
        print(elementos['first']['next']['next']['info'],'\n')
    else:
        print('No se encontraron obras de arte')

def printartistas(elementos):
    size = lt.size(elementos)
    if size:
        print(' Estos son los utlimos tres artistas que se cargaron: ' + '\n')
        print(elementos['first']['info'],'\n')
        print(elementos['first']['next']['info'],'\n')
        print(elementos['first']['next']['next']['info'],'\n')
    else:
        print('No se encontraron artistas')

def print_nacidos(elementos):
    size = lt.size(elementos)
    if size:
        print(' Estos son los ultimos  artistas nacidos en el rango proporcionado: ')
        for artista in lt.iterator(elementos):
            print('Nombre: ' + artista['DisplayName'] + '  Nacio: ' +
                  artista['BeginDate'] + ' Nacionalidad: ' + artista['Nationality'] + ' Genero: ' + artista['Gender'])
    else:
        print('No se encontraron artistas nacidos')

def print_nacidosprimeros(elementos):
    size = lt.size(elementos)
    if size:
        print(' Estos son los primeros  artistas nacidos en el rango proporcionado: ')
        for artista in lt.iterator(elementos):
            print('Nombre: ' + artista['DisplayName'] + '  Nacio: ' +
                  artista['BeginDate'] + ' Nacionalidad: ' + artista['Nationality'] + ' Genero: ' + artista['Gender'])
    else:
        print('No se encontraron artistas nacidos')

def print_obras_delautor(elementos):
    size = lt.size(elementos)
    if size:
        print( '\n' +' Esta es la lista de las obras del autor que fueron hechas con la  misma tecnica: ')
        for artista in lt.iterator(elementos):
            print('Titulo: ' + artista['Title'] + '  Fecha: ' +
                  artista['Date'] + ' Medio: ' + artista['Medium'] + ' Dimensiones: ' + artista['Dimensions'] + '\n')
    else:
        print('No se encontraron artistas nacidos')

def print_tecnicas(elementos):
        print(' Esta es la lista de las tecnicas usadas del autor: ' + '\n')
        for artista in elementos:
            print('Titulo: ' + artista + '  Cantidad: ' + str(elementos[artista]) + '\n')

def print_obras_costosas(elementos,catalogo):
    size = lt.size(elementos)
    if size:
        print( '\n' +' Esta es la lista de las 5 obras mas costosas de departamento: ')
        for artista in lt.iterator(elementos):
            nombres = controller.buscar_artistas(artista['artistas'],catalogo)
            artistas = ''
            for nombre in lt.iterator(nombres):
                if lt.size(nombres) > 1:
                    artistas += nombre + ', '
                else: artistas = nombre
            if artista['tecnica'] == '':
                tecnica = 'Unknown'
            else: 
                tecnica = artista['tecnica']
            print('Titulo: ' + artista['titulo'] + '  artistas: ' +
                  artistas + ' clasificacion: ' + artista['clasificacion'] + ' fecha: ' + 
                  artista['fecha'] + ' Dimensiones: ' + artista['dimensiones'] 
                  + ' tecnica: ' + tecnica + ' costo: ' + str(float(artista['costo'])) + '\n')
    

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ...." + '\n')
        catalog = initCatalog()
        loadData(catalog)
        print('Obras de Arte Cargadas cargados: ' + str(lt.size(catalog['obra_de_arte'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artista'])))
        obras_arte = controller.obtener_ultimos_artes(catalog)
        printobras_arte(obras_arte)
        tres_artistas = controller.obtener_ultimos_artistas(catalog)
        printartistas(tres_artistas)

    elif int(inputs[0]) == 2:

        catalog = initCatalog()
        loadData(catalog)
        año_inicial = input("Porfavor, dijite el año inical del rango que desea buscar: ")
        año_final = input("Porfavor, dijite el año final del rango que desea buscar: ")
        artistas = controller.nacidos_rango(catalog,int(año_inicial),int(año_final))
        print('Total de artistas nacidos en el rango dado: ' + str(lt.size(artistas)) + '\n')

        if lt.isEmpty(artistas):
            print('No nacio ningun artista en este rango')
        elif lt.size(artistas) < 6:
            print_nacidosprimeros(artistas)
        else: 
            primeros_nacidos = controller.obtener_primeros_nacidos(artistas)
            print_nacidosprimeros(primeros_nacidos)
            ultimos_nacidos = controller.obtener_ultimos_nacidos(artistas)
            print_nacidos(ultimos_nacidos)

    elif int(inputs[0]) == 3:
        fecha_inicial = input("Porfavor, dijite la fecha inical del rango que ddesea buscar (Formato: Año/Mes/Dia): ")
        fecha_final = input("Porfavor, dijite la fecha final del rango que ddesea buscar (Formato: Año/Mes/Dia): ")
    elif int(inputs[0]) == 4:
        Artista = input("Porfavor, dijite el nombre del artista que desea buscar")
        catalog = initCatalog()
        loadData(catalog)
        artista_final = controller.consulta_codigo(catalog,Artista)

        print('\n' +'Total de obras del artista: ' + str(lt.size(artista_final['obras'])) + '\n')

        diccionario_tecnicas = controller.cantidad_tecnicas_cada(artista_final)

        print_tecnicas(diccionario_tecnicas)

        tecnicas = controller.cantidad_tecnicas(artista_final)

        print('La tecnica mas utilizada por el autor fue: ' + str(tecnicas) + '\n')

        obras = controller.consulta_obras(artista_final,tecnicas)

        print_obras_delautor(obras)

    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        Departamento = input("Porfavor, dijite el deprtamento que desea conocer el costo del tranposrte")
        catalog = initCatalog()
        loadData(catalog)

        filtradas = controller.filtrar_depto(catalog,Departamento)
        costo = controller.calculo_de_transporte(filtradas)
        ordenadas = controller.sortcostos(costo)

        print('El total de obras a trasnportar es de: ' + str(lt.size(ordenadas)) + '\n')
        costo_total = controller.suma_costo(ordenadas)
        print('El costo total del transporte es de: ' + str(costo_total) + '\n')
        peso_total = controller.suma_peso(ordenadas)
        print('El peso total de trasnporte es de: ' + str(peso_total) + '\n')
        costosas = controller.obtener_costosas(ordenadas)
        print_obras_costosas(costosas,catalog)

        orden = controller.obtener_antiguas(ordenadas)
        print_obras_costosas(orden,catalog)


    elif int(inputs[0]) == 7:
        año_inicial = input("Porfavor, dijite el año inical del rango que ddesea buscar: ")
        año_final = input("Porfavor, dijite el año final del rango que ddesea buscar: ") 
        area = input("Porfavor, dijite el area disponible para generar la nueva exhibicion: ")  
    else:
        sys.exit(0)
sys.exit(0)
