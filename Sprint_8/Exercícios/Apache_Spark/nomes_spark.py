from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import col,lit,rand,when

spark = SparkSession \
         .builder \
         .master("local[*]")\
         .appName("Exercício Intro") \
         .getOrCreate()

#ETAPA 01
df_nomes = spark.read.csv("C:\\Users\\bianc\\PycharmProjects\\BiancaLages\\Sprint_8\\Exercícios\\Apache_Spark\\nomes_aleatorios.txt", header=False, inferSchema=True)

#ETAPA 02
df_nomes = df_nomes.withColumnRenamed('_c0','Nomes')

#ETAPA 03
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() <= 0.33, lit("Fundamental"))
    .when((rand() > 0.33) & (rand() <= 0.66), lit("Médio"))
    .otherwise(lit("Superior"))
)

#ETAPA 04
paises_sul_america = ["Brasil", "Argentina", "Bolívia", "Chile", "Colômbia", "Equador",
                      "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() <= 1/13, lit("Brasil"))
    .when(rand() <= 1/13, lit("Argentina"))
    .when(rand() <= 1/13, lit("Bolivia"))
    .when(rand() <= 1/13, lit("Chile"))
    .when(rand() <= 1/13, lit("Colombia"))
    .when(rand() <= 1/13, lit("Equador"))
    .when(rand() <= 1/13, lit("Guiana"))
    .when(rand() <= 1/13, lit("Paraguai"))
    .when(rand() <= 1/13, lit("Peru"))
    .when(rand() <= 1/13, lit("Suriname"))
    .when(rand() <= 1/13, lit("Uruguai"))
    .when(rand() <= 1/13, lit("Venezuela"))
    .otherwise(lit("Venezuela"))

)
#ETAPA 05
df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * 65 + 1945).cast("int"))

#ETAPA 06
df_select = df_nomes.filter(col("AnoNascimento") >= 2001)
df_select.select("Nomes").show(10)

#ETAPA 07
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select * from pessoas").show()
spark.sql("select * from pessoas where AnoNascimento >= 2001").show()

#ETAPA 08
millennials = df_nomes.filter((col("AnoNascimento") >= 1980) &(col("AnoNascimento") <= 1994))
num_millenials = millennials.count()
print("Número de Millennials: ", num_millenials)

#ETAPA 09
resultado = spark.sql("""
    select count(*) as num_millenials
    from pessoas
    where AnoNascimento BETWEEN 1980 and 1994
""")
resultado.show()

#ETAPA 10
resposta = spark.sql("""
    select 
        Pais,
        case 
            when AnoNaScimento BETWEEN 1944 AND 1964 THEN "Baby Boomers"
            when AnoNascimento BETWEEN 1965 AND 1979 THEN "Geração X"
            when AnoNascimento BETWEEN 1980 AND 1994 THEN "Millenials"
            when AnoNascimento BETWEEN 1995 AND 2015 THEN "Geração Z"
            else "Outras Gerações"
        end as geracao,
        count(*) as quantidade
    from pessoas
    group by Pais, geracao
    order by Pais, geracao , quantidade
""")
resposta.show()