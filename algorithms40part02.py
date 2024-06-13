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

