# import findspark
# from pyspark.sql import SparkSession
#
# wordList = ["python", "java", "ottawa", "news", "java", "ottawa"]
#
# findspark.init()
# spark = SparkSession.builder.master("local[*]").getOrCreate()
# sc = spark.sparkContext
#
# wordsRDD = sc.parallelize(wordList, 4)
#
# print(wordsRDD.collect())
#
# wordPairs = wordsRDD.map(lambda w: (w, 1))
# print(wordPairs.collect())
#
# wordCountsCollected = wordPairs.reduceByKey(lambda x, y: x + y)
# print(wordCountsCollected.collect())

#travelling salesman problem

import random
from itertools import permutations

import inline
from pyspark.pandas.plot import matplotlib

alltours = permutations
def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i]) for i in range(len(aTour)))

aCity = complex

def distance_points(first, second): return abs(first - second)

def generate_cities(number_of_cities):
    seed = 111; width = 500; height = 300
    random.seed(number_of_cities, seed)
    return frozenset(aCity(random.randint(1, width), random.randint(1, height)) for c in range(number_of_cities))

def brute_force(cities):
    "Создать все возможные маршруты по городам и выбрать самый короткий"
    return shortest_tour(alltours(cities))

def shortest_tour(tours): return min(tours, key=distance_tour())

#matplotlib inline
#% matplotlib inline
import matplotlib.pyplot as plt

def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figsize=(15, 10))
    start = tour[0: 1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')

def visualize_segment(segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

def X(city): "X axis"; return city.real
def Y(city): "Y axis"; return city.imag


#pip install pyarrow