import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_date, split, explode, year, month, dayofmonth, row_number, array_contains
from pyspark.sql.window import Window
from datetime import datetime
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

print("Iniciando o job")

# Caminhos dos dados na Trusted Zone
csv_path = "s3://datalake.biancalages/TRUSTED/CSV/2024/11/26/"
json_path = "s3://datalake.biancalages/TRUSTED/JSON/2024/12/06/"

# Ler dados CSV e JSON da Trusted Zone como DynamicFrames
print("Lendo dados CSV da Trusted Zone")
dyf_csv = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [csv_path]},
    format="parquet"
)

print("Lendo dados JSON da Trusted Zone")
dyf_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="parquet"
)

# Converter DynamicFrames para DataFrames
df_csv = dyf_csv.toDF()
df_json = dyf_json.toDF()

# Transformação dados CSV
df_csv = df_csv.withColumn("notamedia", col("notamedia").cast("float")) \
               .withColumn("anolancamento", col("anolancamento").cast("int")) \
               .withColumn("tempominutos", col("tempominutos").cast("int")) \
               .withColumn("numerovotos", col("numerovotos").cast("int")) \
               .withColumn("genero", split(col("genero"), ",").cast("array<string>"))

# Transformação dados JSON
df_json = df_json.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd")) \
                 .withColumnRenamed("id", "json_id") \
                 .withColumnRenamed("name", "json_name")

df_json = df_json.select("json_id", "json_name", "iso_3166_1", "english_name", "language_id", "backdrop_path",
                         "budget", "imdb_id", "original_language", "original_title", "popularity", "release_date",
                         "title", "vote_average", "vote_count", "revenue_int", "revenue_long", "genre_id", "genre_name",
                         "language_name")

# Filtrando os filmes em comum
print("Filmes em comum entre CSV e JSON")
df_comum = df_csv.join(df_json, df_csv["titulopincipal"] == df_json["title"], "inner")

df_comum.show(10)

#TABELA GÊNERO
# Explodir a coluna genero
df_generos = df_comum.select("id", explode(col("genero")).alias("genero"))

# Criar DataFrame com gêneros distintos
df_generos_distinct = df_generos.select("genero").distinct()

# Adicionar coluna de ID para cada gênero encontrado
windowSpecGenero = Window.orderBy("genero")
df_generos_id = df_generos_distinct.withColumn("genre_id", row_number().over(windowSpecGenero))

# Mostrar o DataFrame resultante
df_generos_id.show()

# TABELA IDIOMA
# Criar DataFrame de idiomas com colunas originais e idioma distinto
df_idioma = df_comum.select(
    col("language_id").alias("sigla_language"),
    col("language_name")
).distinct()

# Adicionar coluna de ID para cada idioma
windowSpecIdioma = Window.orderBy("language_name")
df_idioma = df_idioma.withColumn("id_language", row_number().over(windowSpecIdioma))

# Exibir o DataFrame resultante
df_idioma.show()

#TABELA TEMPO
# Selecionar a coluna release_date do df_comum e remover duplicatas
df_tempo = df_comum.select("release_date").distinct()

# Adicionar colunas de ano, mês e dia extraídas de release_date
df_tempo = df_tempo.withColumn("ano", year(col("release_date"))) \
                   .withColumn("mes", month(col("release_date"))) \
                   .withColumn("dia", dayofmonth(col("release_date")))

# Adicionar coluna de id_tempo auto-incrementada
windowSpecTempo = Window.orderBy("release_date")
df_tempo = df_tempo.withColumn("id_tempo", row_number().over(windowSpecTempo))

# Exibir o DataFrame resultante
df_tempo.show()

#TABELA FILMES

# Selecionar e renomear colunas do df_comum
df_filmes_base = df_comum.select(
    col("id").alias("id_filmes"),
    col("titulopincipal").alias("tituloprincipal"),
    col("tituloOriginal"),
    col("budget"),
    col("tempominutos"),
    col("vote_average"),
    col("vote_count"),
    col("revenue_int"),
    col("popularity"),
    col("release_date"),
    col("language_id")
)

# Juntar com df_tempo para obter id_tempo
df_filmes_with_tempo = df_filmes_base.join(
    df_tempo.select("release_date", "id_tempo"),
    on="release_date",
    how="left"
)

# Juntar com df_idioma para obter silga_language
df_filmes = df_filmes_with_tempo.join(
    df_idioma,
    df_filmes_with_tempo["language_id"] == df_idioma["sigla_language"],
    how="left"
).drop(df_idioma["sigla_language"])

df_filmes = df_filmes.withColumn("lucro", col("revenue_int") - col("budget"))

# Selecionar as colunas finais
df_filmes = df_filmes.select(
    col("id_filmes"),
    col("tituloprincipal"),
    col("tituloOriginal"),
    col("budget"),
     col("revenue_int"),
    col("tempominutos"),
    col("vote_average"),
    col("vote_count"),
    col("popularity"),
    col("lucro"),
    col("id_tempo"),
    col("id_language")
)

#Removendo as duplicadas
df_filmes = df_filmes.dropDuplicates(["tituloprincipal"])

# Exibir o DataFrame resultante
df_filmes.show()

#TABELA RELACIONAL FILMES E GENEROS
# Explodir a coluna genero em df_comum para criar linhas individuais para cada gênero
df_filmes_genero_base = df_comum.select(
    col("id").alias("id_filmes"),
    explode(col("genero")).alias("genero")
)

# Unir com a tabela de gêneros para obter genre_id
df_filmes_genero = df_filmes_genero_base.join(
    df_generos_id,
    on="genero",
    how="left"
).select(
    col("id_filmes"),
    col("genre_id")
)

# Remover duplicatas para garantir um relacionamento de um para muitos
df_filme_generos = df_filmes_genero.dropDuplicates()

# Exibir o DataFrame resultante
df_filme_generos.show()

# Converter DataFrames para DynamicFrames
dyf_comum = DynamicFrame.fromDF(df_comum, glueContext, "dyf_union")
dyf_tempo = DynamicFrame.fromDF(df_tempo, glueContext, "dyf_tempo")
dyf_filmes = DynamicFrame.fromDF(df_filmes, glueContext, "dyf_filmes")
dyf_idioma = DynamicFrame.fromDF(df_idioma, glueContext, "dyf_idioma")
dyf_genero = DynamicFrame.fromDF(df_generos_id, glueContext, "dyf_genero")
dyf_filme_generos = DynamicFrame.fromDF(df_filme_generos, glueContext, "dyf_filme_generos")

# Caminho de saída na Refined Zone com pastas para cada tabela e depois o dia de processamento
refined_path = "s3://datalake.biancalages/REFINED/MRD/"
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

# Escrever DynamicFrames na Refined Zone
print("Escrevendo dados na Refined Zone")

glueContext.write_dynamic_frame.from_options(
    frame=dyf_comum,
    connection_type="s3",
    connection_options={"path": f"s3://datalake.biancalages/UNION/PARQUET/{year}/{month}/{day}/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_tempo,
    connection_type="s3",
    connection_options={"path": f"{refined_path}TEMPO/{year}/{month}/{day}/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_filmes,
    connection_type="s3",
    connection_options={"path": f"{refined_path}FILMES_FATO/{year}/{month}/{day}/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_idioma,
    connection_type="s3",
    connection_options={"path": f"{refined_path}IDIOMAS/{year}/{month}/{day}/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_genero,
    connection_type="s3",
    connection_options={"path": f"{refined_path}GENEROS/{year}/{month}/{day}/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_filme_generos,
    connection_type="s3",
    connection_options={"path": f"{refined_path}FILME_GENEROS_RELACIONAL/{year}/{month}/{day}/"},
    format="parquet"
)

print("Job concluído com sucesso")
job.commit()
