from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, length, col

#Inicia a Sessão Pyspark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

#Leitura do arquivo README
readme_df = spark.read.text("../../Sprint_1/Desafio/README.md")

#Filtro e contagem de palavras do arquivo README
words = readme_df.select(explode(split(col("value"),"\\s+")).alias("word"))
filtro_words = words.filter(length(col("word")) > 3)
words_count = filtro_words.groupBy("word").count()
words_count = words_count.orderBy(col("count").desc())

#Mostra a tabela de contagem de palavras
words_count.show()

#Encerra a sessão Pyspark
spark.stop()