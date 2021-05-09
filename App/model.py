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
import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura del analizador de eventos
"""

# Construcción de modelo

def newAnalyzer():
    """
    Inicializa el analizador de eventos
    """
    analyzer = {'events': None,
                'event': None,
                'tracks': None,
                'artists': None,
                'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'energy': None,
                'time': None,
                'hashtags': None,
                'vaders': None}
    
    """
    Se crea una lista vacía para guardar los eventos
    """
    analyzer['events'] = lt.newList('ARRAY_LIST')

    """
    Se crean maps para acceder a la información de los eventos
    """
    analyzer['event'] = mp.newMap(maptype='PROBING')
    analyzer['tracks'] = mp.newMap(maptype='PROBING')
    analyzer['artists'] = mp.newMap(maptype='PROBING')
    analyzer['instrumentalness'] = om.newMap('RBT', compareValues)
    analyzer['liveness'] = om.newMap('RBT', compareValues)
    analyzer['speechiness'] = om.newMap('RBT', compareValues)
    analyzer['danceability'] = om.newMap('RBT', compareValues)
    analyzer['valence'] = om.newMap('RBT', compareValues)
    analyzer['loudness'] = om.newMap('RBT', compareValues)
    analyzer['tempo'] = om.newMap('RBT', compareValues)
    analyzer['acousticness'] = om.newMap('RBT', compareValues)
    analyzer['energy'] = om.newMap('RBT', compareValues)
    analyzer['time'] = om.newMap('RBT', compareValues)
    analyzer['hashtags'] = mp.newMap(maptype='PROBING')
    analyzer['vaders'] = mp.newMap(maptype='PROBING')

    return analyzer

# Funciones para agregar información al analizador

def addEvent(analyzer, event):
    """
    Adiciona un evento a la lista de eventos, adicionalmente crea
    entradas en los maps por característica de contenido
    """
    key = event['user_id'] + event['track_id'] + event['created_at']
    existevent = mp.contains(analyzer['event'], key)
    if existevent == False:
        lt.addLast(analyzer['events'], event)
        mp.put(analyzer['event'], key, event)
        addTracks(analyzer, event)
        addArtists(analyzer, event)
        addContentFeature(analyzer, event, 'instrumentalness')
        addContentFeature(analyzer, event, 'liveness')
        addContentFeature(analyzer, event, 'speechiness')
        addContentFeature(analyzer, event, 'danceability')
        addContentFeature(analyzer, event, 'valence')
        addContentFeature(analyzer, event, 'loudness')
        addContentFeature(analyzer, event, 'tempo')
        addContentFeature(analyzer, event, 'acousticness')
        addContentFeature(analyzer, event, 'energy')
        addTime(analyzer, event)

def addTracks(analyzer, event):
    """
    Adiciona un evento a la lista de eventos de una pista específica,
    las pistas se guardan en un map
    """
    tracks = analyzer['tracks']
    track = event['track_id']
    existtrack = mp.contains(tracks, track)
    if existtrack:
        entry = mp.get(tracks, track)
        value = me.getValue(entry)
    else:
        value = newValue(track)
        mp.put(tracks, track, value)
    lt.addLast(value['events'], event)

def addArtists(analyzer, event):
    """
    Adiciona un evento a la lista de eventos de un artista específico,
    los artistas se guardan en un map
    """
    artists = analyzer['artists']
    artist = event['artist_id']
    existartist = mp.contains(artists, artist)
    if existartist:
        entry = mp.get(artists, artist)
        value = me.getValue(entry)
    else:
        value = newValue(artist)
        mp.put(artists, artist, value)
    lt.addLast(value['events'], event)

def addContentFeature(analyzer, event, feature):
    """
    Adiciona un evento a la lista de eventos de una característica de
    contenido específica, las características de contenido se
    guardan en un árbol tipo 'RBT'
    """
    map = analyzer[feature]
    key = float(event[feature])
    existkey = om.contains(map, key)
    if existkey:
        entry = om.get(map, key)
        value = me.getValue(entry)
    else:
        value = newValue(key)
        om.put(map, key, value)
    lt.addLast(value['events'], event)

def addTime(analyzer, event):
    """
    Adiciona un evento a la lista de eventos de una hora de creación
    específica, las horas de creación se guardan en un árbol
    tipo 'RBT'
    """
    map = analyzer['time']
    date = event['created_at']
    time = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').time()
    existtime = om.contains(map, time)
    if existtime:
        entry = om.get(map, time)
        value = me.getValue(entry)
    else:
        value = newValue(time)
        om.put(map, time, value)
    lt.addLast(value['events'], event)

def addHashtag(analyzer, hashtag):
    """
    Adiciona un hashtag al map de hashtags
    """
    mp.put(analyzer['hashtags'], hashtag['hashtag'], hashtag)

def addSentimentValue(analyzer, sentimentvalue):
    """
    Adiciona el valor promedio vader al map de vaders
    """
    mp.put(analyzer['vaders'], sentimentvalue['hashtag'], sentimentvalue['vader_avg'])

# Funciones para creación de datos

def newValue(value):
    """
    Esta función crea la estructura de eventos asociados
    a un map específico
    """
    value = {'events': None}
    value['events'] = lt.newList('ARRAY_LIST')
    return value

# Funciones de consulta

def eventsSize(analyzer):
    """
    Retorna el número de eventos cargados en el
    analizador
    """
    return lt.size(analyzer['events'])

def tracksSize(analyzer):
    """
    Retorna el número de pistas cargadas en el
    analizador
    """
    return mp.size(analyzer['tracks'])

def artistsSize(analyzer):
    """
    Retorna el número de artistas cargados en el
    analizador
    """
    return mp.size(analyzer['artists'])

def getEventsByRange(analyzer, feature, initialValue, finalValue):
    """
    Retorna el número de eventos y artistas por característica de contenido
    en un rango de valores
    """
    artists = mp.newMap(maptype='PROBING')
    totalevents = 0
    lst = om.values(analyzer[feature], initialValue, finalValue)
    for lstevents in lt.iterator(lst):
        totalevents += lt.size(lstevents['events'])
        for event in lt.iterator(lstevents['events']):
            artist = event['artist_id']
            mp.put(artists, artist, event)
    totalartists = mp.size(artists)
    artistsids = mp.keySet(artists)
    return totalevents, totalartists, artistsids

def getEventsByEnergyAndDanceability(analyzer, initialValue1, finalValue1, initialValue2, finalValue2):
    """
    Retorna el número de pistas y el map de pistas para las características
    de contenido 'energy' y 'danceability' en un rango de valores
    """
    map = om.newMap('RBT', compareValues)
    lstenergy = om.values(analyzer['energy'], initialValue1, finalValue1)
    for lstevents in lt.iterator(lstenergy):
        for event in lt.iterator(lstevents['events']):
            key = float(event['danceability'])
            existkey = om.contains(map, key)
            if existkey:
                entry = om.get(map, key)
                value = me.getValue(entry)
            else:
                value = newValue(key)
                om.put(map, key, value)
            lt.addLast(value['events'], event)

    tracks = mp.newMap(maptype='PROBING')
    lstdanceability = om.values(map, initialValue2, finalValue2)
    for lstevents in lt.iterator(lstdanceability):
        for event in lt.iterator(lstevents['events']):
            track = event['track_id']
            mp.put(tracks, track, event)
    totaltracks = mp.size(tracks)
    return totaltracks, tracks

def getEventsByInstrumentalnessAndTempo(analyzer, initialValue1, finalValue1, initialValue2, finalValue2):
    """
    Retorna el número de pistas y el map de pistas para las características
    de contenido 'instrumentalness' y 'tempo' en un rango de valores
    """
    map = om.newMap('RBT', compareValues)
    lstinstrumentalness = om.values(analyzer['instrumentalness'], initialValue1, finalValue1)
    for lstevents in lt.iterator(lstinstrumentalness):
        for event in lt.iterator(lstevents['events']):
            key = float(event['tempo'])
            existkey = om.contains(map, key)
            if existkey:
                entry = om.get(map, key)
                value = me.getValue(entry)
            else:
                value = newValue(key)
                om.put(map, key, value)
            lt.addLast(value['events'], event)

    tracks = mp.newMap(maptype='PROBING')
    lsttempo = om.values(map, initialValue2, finalValue2)
    for lstevents in lt.iterator(lsttempo):
        for event in lt.iterator(lstevents['events']):
            track = event['track_id']
            mp.put(tracks, track, event)
    totaltracks = mp.size(tracks)
    return totaltracks, tracks

def getGenres(analyzer, key, initialValue, finalValue, option):
    """
    Adiciona una entrada al map de géneros, donde la llave es el género y
    el valor es una tupla con el número de eventos, el número de
    artistas únicos y los id de los artistas 
    """
    genres = mp.newMap(maptype='PROBING')
    mp.put(genres, 'Reggae', getEventsByRange(analyzer, 'tempo', 60.0, 90.0))
    mp.put(genres, 'Down-tempo', getEventsByRange(analyzer, 'tempo', 70.0, 100.0))
    mp.put(genres, 'Chill-out', getEventsByRange(analyzer, 'tempo', 90.0, 120.0))
    mp.put(genres, 'Hip-hop', getEventsByRange(analyzer, 'tempo', 85.0, 115.0))
    mp.put(genres, 'Jazz and Funk', getEventsByRange(analyzer, 'tempo', 120.0, 125.0))
    mp.put(genres, 'Pop', getEventsByRange(analyzer, 'tempo', 100.0, 130.0))
    mp.put(genres, 'R&B', getEventsByRange(analyzer, 'tempo', 60.0, 80.0))
    mp.put(genres, 'Rock', getEventsByRange(analyzer, 'tempo', 110.0, 140.0))
    mp.put(genres, 'Metal', getEventsByRange(analyzer, 'tempo', 100.0, 160.0))
    if option == True:
        mp.put(genres, str(key), getEventsByRange(analyzer, 'tempo', initialValue, finalValue))
    return genres

def getEventsByTimeRange(analyzer, initialValue, finalValue):
    """
    Retorna el número de eventos y el map de eventos en un rango determinado
    de tiempo en horas, minutos y segundos (%H:%M:%S)
    """
    map = om.newMap('RBT')
    initialTime = datetime.datetime.strptime(initialValue, '%H:%M:%S').time()
    finalTime = datetime.datetime.strptime(finalValue, '%H:%M:%S').time()
    lstevents = om.values(analyzer['time'], initialTime, finalTime)
    totalevents = 0
    for lstevents in lt.iterator(lstevents):
        totalevents += lt.size(lstevents['events'])
        for event in lt.iterator(lstevents['events']):
            key = float(event['tempo'])
            existkey = om.contains(map, key)
            if existkey:
                entry = om.get(map, key)
                value = me.getValue(entry)
            else:
                value = newValue(key)
                om.put(map, key, value)
            lt.addLast(value['events'], event)
    return map, totalevents

def getEventsByTempoRange(map, initialValue, finalValue, genre):
    """
    Retorna el número de eventos, de pistas y los ids de esas pistas
    en un rango de valores por tempo, adicionalmente retorna el
    género respectivo para ese rango de tempo
    """
    tracks = mp.newMap(maptype='PROBING')
    totalevents = 0
    lst = om.values(map, initialValue, finalValue)
    for lstevents in lt.iterator(lst):
        totalevents += lt.size(lstevents['events'])
        for event in lt.iterator(lstevents['events']):
            track = event['track_id']
            mp.put(tracks, track, event)
    totaltracks = mp.size(tracks)
    tracksids = mp.keySet(tracks)
    return genre, totalevents, totaltracks, tracksids

def getEventsByGenre(map):
    """
    Adiciona una entrada al map de géneros, donde la llave es el numero de
    eventos y el valor es una tupla con el género, el número de
    pistas únicas y los id de las pistas. Retorna el map
    de géneros tipo 'RBT'
    """
    genres = om.newMap('RBT', compareValuesDescOrder)
    om.put(genres, getEventsByTempoRange(map, 60.0, 90.0, 'Reggae')[1], 
        getEventsByTempoRange(map, 60.0, 90.0, 'Reggae'))
    om.put(genres, getEventsByTempoRange(map, 70.0, 100.0, 'Down-tempo')[1], 
        getEventsByTempoRange(map, 70.0, 100.0, 'Down-tempo'))
    om.put(genres, getEventsByTempoRange(map, 90.0, 120.0, 'Chill-out')[1], 
        getEventsByTempoRange(map, 90.0, 120.0, 'Chill-out'))
    om.put(genres, getEventsByTempoRange(map, 85.0, 115.0, 'Down-tempo')[1], 
        getEventsByTempoRange(map, 85.0, 115.0, 'Hip-hop'))
    om.put(genres, getEventsByTempoRange(map, 120.0, 125.0, 'Jazz and Funk')[1], 
        getEventsByTempoRange(map, 120.0, 125.0, 'Jazz and Funk'))
    om.put(genres, getEventsByTempoRange(map, 100.0, 130.0, 'Pop')[1], 
        getEventsByTempoRange(map, 100.0, 130.0, 'Pop'))
    om.put(genres, getEventsByTempoRange(map, 60.0, 80.0, 'R&B')[1], 
        getEventsByTempoRange(map, 60.0, 80.0, 'R&B'))
    om.put(genres, getEventsByTempoRange(map, 110.0, 140.0, 'Rock')[1], 
        getEventsByTempoRange(map, 110.0, 140.0, 'Rock'))
    om.put(genres, getEventsByTempoRange(map, 100.0, 160.0, 'Metal')[1], 
        getEventsByTempoRange(map, 100.0, 160.0, 'Metal'))
    return genres

# Funciones de comparación

def compareValues(value1, value2):
    """
    Compara los valores de una característica
    de dos eventos
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1

def compareValuesDescOrder(value1, value2):
    """
    Compara los valores de una característica
    de dos eventos en orden descendiente
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return -1
    else:
        return 1