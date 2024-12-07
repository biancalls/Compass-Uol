import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import col, to_date, when, explode
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho para os dados JSON no S3
json_path = "s3://datalake.biancalages/RAW/TMDB/2024/12/06/"
trusted_path = "s3://datalake.biancalages/TRUSTED/JSON/"

# Ler os dados JSON usando DynamicFrame
print(f"Lendo dados JSON do caminho: {json_path}")
dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="json"
)
print("Dados JSON lidos com sucesso.")
dyf.printSchema()

# Converter DynamicFrame para DataFrame
df = dyf.toDF()
print("Convertido para DataFrame Spark.")
df.show(5)
df.printSchema()

# Converter release_date de string para DateType
df = df.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd"))
print("Coluna release_date convertida para DateType.")

# Remover colunas desnecessárias
df = df.drop("overview", "poster_path", "tagline", "homepage", "runtime", "production_companies", "status", "video", "adult", "belongs_to_collection", "production_countries", "origin_country")

# Substituir budget zero por null
df = df.withColumn("budget", when(col("budget") == 0, None).otherwise(col("budget")))

# Lidar com a coluna revenue
df = df.withColumn("revenue_int", when(col("revenue.int") == 0, None).otherwise(col("revenue.int")))
df = df.withColumn("revenue_long", when(col("revenue.long") == 0, None).otherwise(col("revenue.long")))
df = df.drop("revenue")

print("Colunas budget e revenue ajustadas para mostrar null quando zero.")

# Explodir o array de gêneros
df = df.withColumn("genre", explode("genres"))
df = df.withColumn("genre_id", col("genre.id"))
df = df.withColumn("genre_name", col("genre.name"))
df = df.drop("genres", "genre")

# Explodir o array de idiomas falados
df = df.withColumn("spoken_language", explode("spoken_languages"))
df = df.withColumn("language_id", col("spoken_language.iso_639_1"))
df = df.withColumn("language_name", col("spoken_language.english_name"))
df = df.drop("spoken_languages", "spoken_language")

df.show(5)
df.printSchema()

# Transformar DataFrame de volta para DynamicFrame
dyf_transformed = DynamicFrame.fromDF(df, glueContext, "dyf_transformed")
print("Convertido de volta para DynamicFrame.")
dyf_transformed.printSchema()

# Caminho de saída com base na data de processamento atual
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

output_path = f"{trusted_path}{year}/{month}/{day}/"

# Escrever os dados na camada Trusted em formato PARQUET
glueContext.write_dynamic_frame.from_options(
    frame=dyf_transformed,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)
print("Dados salvos com sucesso no formato PARQUET.")

job.commit()
print("Job concluído com sucesso.")

