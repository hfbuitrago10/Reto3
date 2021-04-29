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
    Se crea una lista para guardar los eventos
    """
    analyzer['events'] = lt.newList('ARRAY_LIST')

    """
    Se crean maps para acceder a la información de los eventos
    """
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
    Adiciona un evento a la lista de eventos
    """
    lt.addLast(analyzer['events'], event)
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
    Adiciona un evento a la lista de eventos de una caracteristica de
    contenido específica, las caracteristicas de contenido se
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