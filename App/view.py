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
        año_inicial = input("Porfavor, dijite el año inical del rango que ddesea buscar: ")
        año_final = input("Porfavor, dijite el año final del rango que ddesea buscar: ") 
    elif int(inputs[0]) == 3:
        fecha_inicial = input("Porfavor, dijite la fecha inical del rango que ddesea buscar (Formato: Año/Mes/Dia): ")
        fecha_final = input("Porfavor, dijite la fecha final del rango que ddesea buscar (Formato: Año/Mes/Dia): ")
    elif int(inputs[0]) == 4:
        Artista = input("Porfavor, dijite el nombre del artista qeu desea buscar")
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        Artista = input("Porfavor, dijite el deprtamento que desea conocer el costo del tranposrte")
    elif int(inputs[0]) == 7:
        año_inicial = input("Porfavor, dijite el año inical del rango que ddesea buscar: ")
        año_final = input("Porfavor, dijite el año final del rango que ddesea buscar: ") 
        area = input("Porfavor, dijite el area disponible para generar la nueva exhibicion: ")  
    else:
        sys.exit(0)
sys.exit(0)
