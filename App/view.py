"""
 * Copyright 2021, Departamento de Sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program. If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
assert cf

"""
La vista se encarga de la interacción con el usuario
"""

# Menú de opciones

def printMenu():
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información de los eventos")
    print("3- Consultar eventos por característica en un rango")
    print("4- Consultar pistas por energy y danceability")
    print("5- Consultar pistas por instrumentalness y tempo")
    print("6- Consultar pistas y artistas por género")
    print("7- Consultar género más escuchado en un rango de horas")
    print("0- Salir")

# Funciones de inicialización

def initAnalyzer():
    """
    Inicializa el analizador de eventos
    """
    return controller.initAnalyzer()

def loadData(analyzer):
    """
    Carga la información de los eventos al analizador
    """
    return controller.loadData(analyzer)

analyzer = None

"""
Menú principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print()
        print("Inicializando....\n")
        analyzer = initAnalyzer()

    elif int(inputs[0]) == 2:
        print()
        print("Cargando información de los eventos....")
        data = loadData(analyzer)
        print("\nTotal de eventos cargados: " + str(controller.eventsSize(analyzer)))
        print("Total de artistas cargados: " + str(controller.artistsSize(analyzer)))
        print("Total de pistas cargadas: " + str(controller.tracksSize(analyzer)) + "\n")

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)