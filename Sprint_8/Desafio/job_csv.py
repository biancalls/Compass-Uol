import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_timestamp, date_format, col, lit
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

csv_path = "s3://datalake.biancalages/RAW/Local/CSV/Movies/11/11/2024/movies.csv"
trusted_path = 's3://datalake.biancalages/TRUSTED/CSV/'

# Definir o esquema manualmente
schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

df = spark.read.format('csv').option('header', 'true').option('delimiter', '|').schema(schema).load(csv_path)

# Remover duplicatas com base no título original
df = df.dropDuplicates(['tituloOriginal'])

# Remover colunas indesejadas
df = df.drop('generoArtista', 'personagem', 'anoNascimento', 'anoFalecimento', 'profissao')

# Gerar strings para o caminho de saída com base na data atual
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

trusted_zone_path = f'{trusted_path}{year}/{month}/{day}/'

# Gravar os dados na camada Trusted em formato PARQUET
df.write.mode('overwrite').parquet(trusted_zone_path)

job.commit()