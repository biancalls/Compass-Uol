import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, upper, desc, max as spark_max, count
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = spark.read.csv(source_file, header=True, inferSchema=True)
# Imprimir o schema
df.printSchema()

# Alterar os valores da coluna "nome" para maiúsculas
df_upper = df.withColumn("nome", upper(col("nome")))

# Contar o número de linhas
linhas_countagem = df_upper.count()
print(f"Contagem de linhas: {linhas_countagem}")

# Contar nomes agrupados por "ano" e "sexo"
df_grouped = df_upper.groupBy("ano", "sexo").agg(count("nome").alias("contagem_nomes"))

# Ordenar pelos anos mais recentes
df_sorted = df_grouped.orderBy(desc("ano"))
df_sorted.show()

# Nome feminino mais frequente
feminino_mais_frequente = df_upper.filter(col("sexo") == "F") \
    .groupBy("nome", "ano").agg(spark_max("total").alias("max_frequencia")) \
    .orderBy(desc("max_frequencia")) \
    .first()

# Nome masculino mais frequente
masculino_mais_frequente = df_upper.filter(col("sexo") == "M") \
    .groupBy("nome", "ano").agg(spark_max("total").alias("max_frequencia")) \
    .orderBy(desc("max_frequencia")) \
    .first()

print(f"Nome feminino mais frequente: {feminino_mais_frequente['nome']}, Ano: {feminino_mais_frequente['ano']}")
print(f"Nome masculino mais frequente: {masculino_mais_frequente['nome']}, Ano: {masculino_mais_frequente['ano']}")

# Total de registros por ano
total_por_ano = df_upper.groupBy("ano", "sexo").agg(count("nome").alias("total_registros"))
total_por_ano_sorted = total_por_ano.orderBy("ano").limit(10)
total_por_ano_sorted.show()

# Caminho de saída no S3
target_path = "s3://sprint05.com/lab-glue/frequencia_registro_nomes_eua"

# Escrever no S3 em formato JSON com particionamento por "sexo" e "ano"
df_upper.write.mode("overwrite") \
    .partitionBy("sexo", "ano") \
    .json(target_path)

job.commit()