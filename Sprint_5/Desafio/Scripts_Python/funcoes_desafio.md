```python
import numpy as np
import boto3
from io import StringIO
import os

# Definindo as variáveis de ambiente
AWS_ACCESS_KEY_ID = os.environ.get("ASIAXZEFHX2RGGMSDLKC")
AWS_SECRET_ACCESS_KEY = os.environ.get("bpGmuQqDqibM2i57Sw30+YOVOrT6/aEokGq5mR8N")
AWS_SESSION_TOKEN = os.environ.get(
    "IQoJb3JpZ2luX2VjEFYaCXVzLWVhc3QtMSJHMEUCIF7lNPCHGRSxcKf9NKW1UHBbfbzcG7NUMMCTKBfYMEc+AiEA9ELaWtIAyu0Ez9m4nDAN0DbbWrQ+QjOd3xXz8bbOvMwqpgMIv///////////ARAAGgw1MzUwMDI4NTcxMjIiDAys5aBL/0m+8euGiSr6AokRa0dRh3J/HHzKsVDYn+H583/g+YHDVB50tj31SoL1/Uui++4HBKaeMkSbzbuL6R1YySaj8b5lnW58aj5sCsQ7gQGn9TTQXm3X6jtDsDsHqIcFYDP7zTtEw84xFOQqsC2DcYLvOhmPm0+vrVv+TyKUMrj4wg9PYJf/myMH9j5ppI4ZLlSgEYHCUo1FASN6hD/A8XELzgV2evFq+GBZzkezypVdul+8jr/E04hLNTt+NYcmkiwhzl9ao14N+4dP+8y4qn4rM1W6hz3CjNTBz6OMhVPGef8qzAv3We+d/6RINdsQVdJiHqsrCTf7F+7IjGGPbykcN5qhGgFwX5CNf/wIEpryQYC9BAPHkwUNdA3GykcwyhhkFRxw3gVpo8VC9PCIeCsdDk9qysf0X+/gUO9Q4VoBtrG2Ss+noV+nT1iJvprDVPVSjDr8CAGqtm44SFUIr36ZgWgsmXr+zz/+R0Ex+3x/iIvxbU6Da8zzuahi8zvzXwNdLR/67jCHg+S4BjqmAc/RbZOe2ofaaMT116VSBzONEeYLRYrVLXRm4jIN/P8NkP+USnSmh/WOuw+uD+P00xjllUO44rACKQbkptFmx+X27D6+MYHRYvNX+jJP8IjBZ4HHX1XwwjgkyQyx1Iw0tr8kvkKZ4Elkt8WanlK8jjhbaslb/AqWnDGDHab4Xr8vip9a8aUDCP4P2SCirKuR3ZPBaC7Z12pwaJD2QiiHZG/YNQl4Rrk=")

# Criando a sessão do boto3
session = boto3.Session(
    aws_access_key_id="ASIAXZEFHX2RGGMSDLKC",
    aws_secret_access_key="bpGmuQqDqibM2i57Sw30+YOVOrT6/aEokGq5mR8N",
    aws_session_token="IQoJb3JpZ2luX2VjEFYaCXVzLWVhc3QtMSJHMEUCIF7lNPCHGRSxcKf9NKW1UHBbfbzcG7NUMMCTKBfYMEc+AiEA9ELaWtIAyu0Ez9m4nDAN0DbbWrQ+QjOd3xXz8bbOvMwqpgMIv///////////ARAAGgw1MzUwMDI4NTcxMjIiDAys5aBL/0m+8euGiSr6AokRa0dRh3J/HHzKsVDYn+H583/g+YHDVB50tj31SoL1/Uui++4HBKaeMkSbzbuL6R1YySaj8b5lnW58aj5sCsQ7gQGn9TTQXm3X6jtDsDsHqIcFYDP7zTtEw84xFOQqsC2DcYLvOhmPm0+vrVv+TyKUMrj4wg9PYJf/myMH9j5ppI4ZLlSgEYHCUo1FASN6hD/A8XELzgV2evFq+GBZzkezypVdul+8jr/E04hLNTt+NYcmkiwhzl9ao14N+4dP+8y4qn4rM1W6hz3CjNTBz6OMhVPGef8qzAv3We+d/6RINdsQVdJiHqsrCTf7F+7IjGGPbykcN5qhGgFwX5CNf/wIEpryQYC9BAPHkwUNdA3GykcwyhhkFRxw3gVpo8VC9PCIeCsdDk9qysf0X+/gUO9Q4VoBtrG2Ss+noV+nT1iJvprDVPVSjDr8CAGqtm44SFUIr36ZgWgsmXr+zz/+R0Ex+3x/iIvxbU6Da8zzuahi8zvzXwNdLR/67jCHg+S4BjqmAc/RbZOe2ofaaMT116VSBzONEeYLRYrVLXRm4jIN/P8NkP+USnSmh/WOuw+uD+P00xjllUO44rACKQbkptFmx+X27D6+MYHRYvNX+jJP8IjBZ4HHX1XwwjgkyQyx1Iw0tr8kvkKZ4Elkt8WanlK8jjhbaslb/AqWnDGDHab4Xr8vip9a8aUDCP4P2SCirKuR3ZPBaC7Z12pwaJD2QiiHZG/YNQl4Rrk="
)

s3 = session.resource('s3')

# Carregar o arquivo CSV do bucket S3
s3_client = session.client('s3')
bucket_name = 'biancalages05'
arquivo = 'arrecadacao-estado.csv'

# Carregar CSV diretamente do S3
csv_obj = s3_client.get_object(Bucket=bucket_name, Key=arquivo)
csv_content = csv_obj['Body'].read().decode('latin1')
df = pd.read_csv(StringIO(csv_content), delimiter=';', encoding='latin1')

# Converter colunas numéricas para float
numeric_cols = df.columns[3:]  # Seleciona as colunas a partir da terceira
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Renomear colunas
df.rename(columns={'IPI - AUTOMÓVEIS': 'IPI_Automoveis'}, inplace=True)
df['IPI_Automoveis'] = pd.to_numeric(df['IPI_Automoveis'], errors='coerce')
df['IPI - VINCULADO À IMPORTACAO'] = pd.to_numeric(df['IPI - VINCULADO À IMPORTACAO'], errors='coerce')

# ESTADOS COM ARRECADAÇÃO DE IPI- AUTOMÓVEIS ACIMA DE 10 MILHÕES E IPI- VINCULADO À IMPORTAÇÃO ACIMA DE 5 MILHÕES
filtro = (df['IPI_Automoveis'] > 10000000) & (df['IPI - VINCULADO À IMPORTACAO'] > 5000000)
df_filtrados = df[filtro]

# Upload df_filtrados
csv_buffer = StringIO()
df_filtrados.to_csv(csv_buffer, sep=';', index=False)
output_file_key01 = '../Arquivos_csv/df_filtrados.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key01, Body=csv_buffer.getvalue())

print(f'Arquivo {output_file_key01} enviado para o bicket {bucket_name} com sucesso!')

# AGRUPA POR ESTADO E SOMA A IMPORTAÇÃO
df['IMPOSTO SOBRE IMPORTAÇÃO'] = pd.to_numeric(df['IMPOSTO SOBRE IMPORTAÇÃO'], errors='coerce')

agrupado = df.groupby('UF')['IMPOSTO SOBRE IMPORTAÇÃO'].sum()

# Upload df_grouped
csv_buffer = StringIO()
agrupado.to_csv(csv_buffer, sep=';', index=False)
output_file_key02 = '../Arquivos_csv/df_agrupado.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key02, Body=csv_buffer.getvalue())

print(f'Arquivo {output_file_key02} enviado para o bicket {bucket_name} com sucesso!')


# ESTADOS COM ARRECADAÇÃO DE IRPF É MAIOR QUE IRPJ
def arrecadacao_IRPF_IRPJ(df):
    return df[df['IRPF'] > df['IRPJ - DEMAIS EMPRESAS']]


df_IRPF_maior_IRPJ = arrecadacao_IRPF_IRPJ(df)

# Upload df_IRPF_maior_IRPJ
csv_buffer = StringIO()
df_IRPF_maior_IRPJ.to_csv(csv_buffer, sep=';', index=False)
output_file_key03 = '../Arquivos_csv/df_IRPF_maior_IRPJ.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key03, Body=csv_buffer.getvalue())

print(f'Arquivo {output_file_key03} enviado para o bicket {bucket_name} com sucesso!')

# CONVERTENDO VALORES PARA MILHÕES
df.rename(columns={'IMPOSTO SOBRE IMPORTAÇÃO': 'Importacao'}, inplace=True)


def converter_milhoes(valor):
    return valor / 1000000


df['Importação_milhoes'] = df['Importacao'].apply(converter_milhoes)


# ANÁLISE ANUAL por UF POR IMPORTAÇÃO
def ano_UF(df, coluna_valor):
    df_agrupado = df.groupby(['Ano', 'UF'])[coluna_valor].sum().reset_index()
    return df_agrupado


df_agrupado = ano_UF(df, 'Importacao')

# Upload df_agrupado
csv_buffer = StringIO()
df_agrupado.to_csv(csv_buffer, sep=';', index=False)
output_file_key04 = '../Arquivos_csv/df_agrupado.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key04, Body=csv_buffer.getvalue())

print(f'Arquivo {output_file_key04} enviado para o bicket {bucket_name} com sucesso!')


# Função de exemplo para manipulação de strings - Ex: Converter o mês em maiúsculas
def converter_mes_para_maiusculas(df):
    df['Mês'] = df['Mês'].str.upper()
    return df


df = converter_mes_para_maiusculas(df)

# Upload df final
csv_buffer = StringIO()
df.to_csv(csv_buffer, sep=';', index=False)
output_file_key05 = '../Arquivos_csv/df_final.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key05, Body=csv_buffer.getvalue())

print(f'Arquivo {output_file_key05} enviado para o bicket {bucket_name} com sucesso!')

print(f'Upload de DataFrames para o bucket {bucket_name} concluído com sucesso!')

```
