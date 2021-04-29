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
import random
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
assert cf

"""
La vista se encarga de la interacción con el usuario
"""

# Funciones para la impresión de resultados

def printFirstFiveEvents(analyzer):
    """
    Imprime la información de los primeros 5 eventos cargados
    en el analizador
    """
    index = 1
    print("Los primeros 5 eventos cargados son: ")
    while index <= 5:
        event = lt.getElement(analyzer['events'], index)
        print("Track " + str(index) + ": " + str(event['track_id']) + "  Instrumentalness: " +
        str(event['instrumentalness']) + "  Liveness: " + str(event['liveness']) + "  Speechiness: " +
        str(event['speechiness']) + "  Danceability: " + str(event['danceability']) + "  Valence: " + 
        str(event['valence']) + "  Loudness: " + str(event['loudness']) + "  Tempo: " + str(event['tempo']) +
        "  Acousticness: " + str(event['acousticness']) + "  Energy: " + str(event['energy']))
        index += 1
    print()

def printLastFiveEvents(analyzer):
    """
    Imprime la información de los últimos 5 eventos cargados
    en el analizador
    """
    size = lt.size(analyzer['events'])
    index = size - 4
    print("Los últimos 5 eventos cargados son: ")
    while index <= size:
        event = lt.getElement(analyzer['events'], index)
        print("Track " + str(index) + ": " + str(event['track_id']) + "  Instrumentalness: " +
        str(event['instrumentalness']) + "  Liveness: " + str(event['liveness']) + "  Speechiness: " +
        str(event['speechiness']) + "  Danceability: " + str(event['danceability']) + "  Valence: " + 
        str(event['valence']) + "  Loudness: " + str(event['loudness']) + "  Tempo: " + str(event['tempo']) +
        "  Acousticness: " + str(event['acousticness']) + "  Energy: " + str(event['energy']))
        index += 1
    print()

def printFiveRandomTracks(map, feature1, feature2):
    """
    """
    index = 1
    size = mp.size(map)
    keys = mp.keySet(map)
    print("5 pistas únicas aleatorias")
    while index <= 5:
        randomnumber = random.randint(1, size)
        key = lt.getElement(keys, randomnumber)
        entry = mp.get(map, key)
        value = me.getValue(entry)
        print("Track " + str(index) + ": " + str(key) + " con " + str(feature1) + " de " + str(value[feature1]) +
        " y " + str(feature2) + " de " + str(value[feature2]))
        index += 1
    print()

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
        print("Total de artistas únicos cargados: " + str(controller.artistsSize(analyzer)))
        print("Total de pistas únicas cargadas: " + str(controller.tracksSize(analyzer)) + "\n")
        printFirstFiveEvents(analyzer)
        printLastFiveEvents(analyzer)

    elif int(inputs[0]) == 3:
        print()
        feature = str(input("Ingrese característica de contenido: "))
        initialValue = float(input("Valor inicial: "))
        finalValue = float(input("Valor final: "))
        print("\nBuscando eventos en el rango....")
        events = controller.getEventsByRange(analyzer, feature, initialValue, finalValue)
        print("\nPara " + str(feature) + " entre " + str(initialValue) + " y " + str(finalValue))
        print("Total de eventos: " + str(events[0]))
        print("Total de artistas únicos: " + str(events[1]) + "\n")

    elif int(inputs[0]) == 4:
        print()
        print("Ingrese valores de energy")
        initialValue1 = float(input("Valor inicial: "))
        finalValue1 = float(input("Valor final: "))
        print("\nIngrese valores de danceability")
        initialValue2 = float(input("Valor inicial: "))
        finalValue2 = float(input("Valor final: "))
        print("\nBuscando pistas en el rango....")
        tracks = controller.getEventsByEnergyAndDanceability(analyzer, initialValue1, finalValue1, initialValue2, finalValue2)
        print("\nPara energy entre " + str(initialValue1) + " y " + str(finalValue1) + " y danceability entre " +
        str(initialValue2) + " y " + str(finalValue2))
        print("Total de pistas únicas: " + str(tracks[0]) + "\n")
        printFiveRandomTracks(tracks[1], 'energy', 'danceability')

    elif int(inputs[0]) == 5:
        print()
        print("Ingrese valores de instrumentalness")
        initialValue1 = float(input("Valor inicial: "))
        finalValue1 = float(input("Valor final: "))
        print("\nIngrese valores de tempo")
        initialValue2 = float(input("Valor inicial: "))
        finalValue2 = float(input("Valor final: "))
        print("\nBuscando pistas en el rango....")
        tracks = controller.getEventsByInstrumentalnessAndTempo(analyzer, initialValue1, finalValue1, initialValue2, finalValue2)
        print("\nPara instrumentalness entre " + str(initialValue1) + " y " + str(finalValue1) + " y tempo entre " +
        str(initialValue2) + " y " + str(finalValue2))
        print("Total de pistas únicas: " + str(tracks[0]) + "\n")
        printFiveRandomTracks(tracks[1], 'instrumentalness', 'tempo')

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)