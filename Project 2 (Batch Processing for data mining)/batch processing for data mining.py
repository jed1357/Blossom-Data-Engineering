from pyspark.sql.types import BooleanType
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.ml.feature import NGram, Tokenizer
import pandas as pd

#  initialise spark
spark = SparkSession.builder.getOrCreate()


#  read company csv data
companies = spark.read.csv(
            "companies.csv", 
            header=True, inferSchema=True)

#  read alldatas csv data
jobs = spark.read.csv(
            "alldatas.csv", 
            header=True, inferSchema=True)

#   renaming column description
companies = companies.withColumnRenamed('description', 'desc')

#  joining two dataframes
aaa = companies.join(jobs, companies.industry == jobs.description)

#  tokenising column and performing ngrmas
tokens = Tokenizer(inputCol='desc', outputCol='tokens')
nn = NGram(n=2, inputCol='tokens', outputCol='ngrams')

b = tokens.transform(companies)
a = nn.transform(b)
final = a.select(['tokens', 'ngrams']).show(3)

#   function of ngram
def ngrram(dataframe, column, x):
    tokens = Tokenizer(inputCol=column, outputCol='tokens')
    nn = NGram(n=x, inputCol='tokens', outputCol='ngrams')
    b = tokens.transform(dataframe)
    a = nn.transform(b)
    final = a.select(['tokens', 'ngrams']).show(4)
    return final

#  calling ngram function
ngrram(companies, 'desc', 2)


#   splitting the location column
loc = a.select('location', F.split(a['location'], ',')[0].alias('city')).show(10)

#  performing an aggregation on some columns
ff = a.filter(a.desc.isNotNull()).select(['ngrams', 'location']).select(F.explode('ngrams').alias('ngrams'), 'location', F.split(a['location'], ',')[0].alias('city')).groupBy(['ngrams', 'city']).count()

#  displaying results of aggregation
ff.show(5)

#   creating spark dataframes which have 3 columns in the order of frequency
gg = a.filter(a.desc.isNotNull()).select(['ngrams', 'industry']).select(F.explode('ngrams').alias('ngrams'), 'industry', F.split(a['industry'], ',')[0].alias('industries')).groupBy(['ngrams', 'industry']).count()

#  displaying results of aggregation
gg.show()