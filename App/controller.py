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
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo
"""

# Inicialización del analizador de eventos

def initAnalyzer():
    """
    Llama la función de inicialización del analizador
    """
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer):
    """
    Carga los datos de los archivos csv en las estructuras
    de datos
    """
    loadEvents(analyzer)

def loadEvents(analyzer):
    """
    Carga los eventos del archivo csv. Por cada evento se indica al
    modelo que debe adicionarlo al analizador
    """
    eventsfile = cf.data_dir + 'subsamples-small/context_content_features-small.csv'
    input_file = csv.DictReader(open(eventsfile, encoding='utf-8'))
    for event in input_file:
        model.addEvent(analyzer, event)

def loadHashtags(analyzer):
    """
    Carga las etiquetas del archivo csv. Por cada etiqueta se indica al
    modelo que debe adicionarla al analizador
    """
    tagsfile = cf.data_dir + 'subsamples-small/user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for hashtag in input_file:
        model.addHashtag(analyzer, hashtag)

def loadSentimentValues(analyzer):
    """
    Carga los valores de sentimientos del archivo csv. Por cada valor se
    indica al modelo que debe adicionarlo al analizador
    """
    sentimentsfile = cf.data_dir + 'subsamples-samll/sentiment_values.csv'
    input_file = csv.DictReader(open(sentimentsfile, encoding='utf-8'))
    for sentimentvalue in input_file:
        model.addSentimentValue(analyzer, sentimentvalue)

# Funciones de consulta

def eventsSize(analyzer):
    """
    Retorna el número de eventos cargados en el
    analizador
    """
    return model.eventsSize(analyzer)

def tracksSize(analyzer):
    """
    Retorna el número de pistas cargadas en el
    analizador
    """
    return model.tracksSize(analyzer)

def artistsSize(analyzer):
    """
    Retorna el número de artistas cargados en el
    analizador
    """
    return model.artistsSize(analyzer)

def getEventsByRange(analyzer, feature, initialValue, finalValue):
    """
    Retorna el número de eventos y artistas por característica de contenido
    en un rango de valores
    """
    return model.getEventsByRange(analyzer, feature, initialValue, finalValue)

def getEventsByEnergyAndDanceability(analyzer, initialValue1, finalValue1, initialValue2, finalValue2):
    """
    Retorna el número de pistas y el map de pistas para las características
    de contenido energy y danceability en un rango de valores
    """
    return model.getEventsByEnergyAndDanceability(analyzer, initialValue1, finalValue1, initialValue2, finalValue2)

def getEventsByInstrumentalnessAndTempo(analyzer, initialValue1, finalValue1, initialValue2, finalValue2):
    """
    Retorna el número de pistas y el map de pistas para las características
    de contenido instrumentalness y tempo en un rango de valores
    """
    return model.getEventsByInstrumentalnessAndTempo(analyzer, initialValue1, finalValue1, initialValue2, finalValue2)

def getGenres(analyzer):
    """
    Retorna el map de géneros
    """
    return model.getGenres(analyzer)