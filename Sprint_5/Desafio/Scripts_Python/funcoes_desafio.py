import pandas as pd
import numpy as np
import boto3
from io import StringIO
import os

# Definindo as variáveis de ambiente
AWS_ACCESS_KEY_ID = os.environ.get('ASIAXZEFHX2RHO5RUO5Y')
AWS_SECRET_ACCESS_KEY = os.environ.get('RoI5EuNOXEqRboSC7AF/8TilUsNM/pWQ76IK++aZ')
AWS_SESSION_TOKEN = os.environ.get('IQoJb3JpZ2luX2VjEJ3//////////wEaCXVzLWVhc3QtMSJHMEUCIQC7liuctv7g5A5FLrwr9cWLG1W2AKYagAE1rnV/bWCMGwIgKFgaOD7PA0LKMzpOnLK2jxeWdk7+Ooqy/mGL9KYVyjIqnQMIFhAAGgw1MzUwMDI4NTcxMjIiDKwIUb/A4SuADkKGvyr6AmKKojMqcfQPNjAB/JvmoTE8Sm01jnyYk1Pxm9RIFk9PWCZ4asJJ+fHvye42xJkWSgbtO1Kmp01ceA34vQ9Qo1Xl5coVNUR0ZJFoe/mADuIYpY3YQPbB6Zk+sizSt0auWU2vE8xRlyKFn92fMMVokwW1bDXzwKtaF7rNkKljBOXM0JNFrJW9H/KK7dbixiRdIbka0115J1krFIRG55SmBMwt+xaHtWki6+w6euw2VixqaV1S0xYajyNuYyzFsEe2+C6qubY86T7XFHw9JueL78yG/0tbG1cZZGKyWp31ehkuWGyktgI6hfa79dGm+rjXc6/jVif+LYU5xrrOP7aGc6of5tEI1bboYlNv4kRSaKk+x0CAoF0vw23HdF3K9Yy+F0AOYsy6fAOScUnXuX7JXIbO3p1jQhvhOpA8bKXFscxgVFShhL9pUK3wR9lOHkMYlgl/U3c12QtrTLvRbHvGN1wxyA47ewjeoxIb/J0oXdX0hfbbN7kX8d6dnjDqz/O4BjqmAdugE7Sr3Zkjs8kpRGWEtmyNX1c/v6sMO3s/PnR7EyurtWRMtRSZ5cr+VSXydFkiLBLW9FjvJ7E/wATM6mpMbuT0ldBPOLMfUbD2jW56xJngqlDiP5VpvC+DzSejW3bgTvTPWz4zQx3dwEaT2bhxpEbfOEOXcciFKc/h9DuJ4OKnDT9L6QqziuMHTt8DtcHzmR9hv3MPIaYX/NeXW2Wumtoplku6H0g=')
# Criando a sessão do boto3
session = boto3.Session(
    aws_access_key_id='ASIAXZEFHX2RHO5RUO5Y',
    aws_secret_access_key='RoI5EuNOXEqRboSC7AF/8TilUsNM/pWQ76IK++aZ',
    aws_session_token='IQoJb3JpZ2luX2VjEJ3//////////wEaCXVzLWVhc3QtMSJHMEUCIQC7liuctv7g5A5FLrwr9cWLG1W2AKYagAE1rnV/bWCMGwIgKFgaOD7PA0LKMzpOnLK2jxeWdk7+Ooqy/mGL9KYVyjIqnQMIFhAAGgw1MzUwMDI4NTcxMjIiDKwIUb/A4SuADkKGvyr6AmKKojMqcfQPNjAB/JvmoTE8Sm01jnyYk1Pxm9RIFk9PWCZ4asJJ+fHvye42xJkWSgbtO1Kmp01ceA34vQ9Qo1Xl5coVNUR0ZJFoe/mADuIYpY3YQPbB6Zk+sizSt0auWU2vE8xRlyKFn92fMMVokwW1bDXzwKtaF7rNkKljBOXM0JNFrJW9H/KK7dbixiRdIbka0115J1krFIRG55SmBMwt+xaHtWki6+w6euw2VixqaV1S0xYajyNuYyzFsEe2+C6qubY86T7XFHw9JueL78yG/0tbG1cZZGKyWp31ehkuWGyktgI6hfa79dGm+rjXc6/jVif+LYU5xrrOP7aGc6of5tEI1bboYlNv4kRSaKk+x0CAoF0vw23HdF3K9Yy+F0AOYsy6fAOScUnXuX7JXIbO3p1jQhvhOpA8bKXFscxgVFShhL9pUK3wR9lOHkMYlgl/U3c12QtrTLvRbHvGN1wxyA47ewjeoxIb/J0oXdX0hfbbN7kX8d6dnjDqz/O4BjqmAdugE7Sr3Zkjs8kpRGWEtmyNX1c/v6sMO3s/PnR7EyurtWRMtRSZ5cr+VSXydFkiLBLW9FjvJ7E/wATM6mpMbuT0ldBPOLMfUbD2jW56xJngqlDiP5VpvC+DzSejW3bgTvTPWz4zQx3dwEaT2bhxpEbfOEOXcciFKc/h9DuJ4OKnDT9L6QqziuMHTt8DtcHzmR9hv3MPIaYX/NeXW2Wumtoplku6H0g='
)

s3 = session.resource('s3')

# Carregar o arquivo CSV do bucket S3
s3_client = session.client('s3')
bucket_name = 'biancalages05'
arquivo= 'arrecadacao-estado.csv'

# Carregar CSV diretamente do S3
csv_obj = s3_client.get_object(Bucket=bucket_name, Key=arquivo)
csv_content = csv_obj['Body'].read().decode('latin1')
df = pd.read_csv(StringIO(csv_content), delimiter=';', encoding='latin1')

# Converter colunas numéricas para float
numeric_cols = df.columns[3:]  # Seleciona as colunas a partir da terceira
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

#Filtro com dois operadores lógicos
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

df.to_csv('df_filtrados.csv', sep=';', index=False)

print(f'Arquivo {output_file_key01} enviado para o bucket {bucket_name} com sucesso!')

##Função de agregação
# AGRUPA POR ESTADO E SOMA A IMPORTAÇÃO
df['IMPOSTO SOBRE IMPORTAÇÃO'] = pd.to_numeric(df['IMPOSTO SOBRE IMPORTAÇÃO'], errors='coerce')

agregado = df.groupby('UF')['IMPOSTO SOBRE IMPORTAÇÃO'].sum()

# Upload df_grouped
csv_buffer = StringIO()
agregado.to_csv(csv_buffer, sep=';', index=False)
output_file_key02 = '../Arquivos_csv/df_agregado.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key02, Body=csv_buffer.getvalue())

df.to_csv('df_agregado.csv', sep=';', index=False)

print(f'Arquivo {output_file_key02} enviado para o bucket {bucket_name} com sucesso!')

##Função Condicional
# ESTADOS COM ARRECADAÇÃO DE IRPF É MAIOR QUE IRPJ
def arrecadacao_IRPF_IRPJ(df):
    return df[df['IRPF'] > df['IRPJ - DEMAIS EMPRESAS']]

df_IRPF_maior_IRPJ = arrecadacao_IRPF_IRPJ(df)

# Upload df_IRPF_maior_IRPJ
csv_buffer = StringIO()
df_IRPF_maior_IRPJ.to_csv(csv_buffer, sep=';', index=False)
output_file_key03 = '../Arquivos_csv/df_IRPF_maior_IRPJ.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_file_key03, Body=csv_buffer.getvalue())

df.to_csv('df_IRPF_maior_IRPJ.csv', sep=';', index=False)

print(f'Arquivo {output_file_key03} enviado para o bucket {bucket_name} com sucesso!')

#Função de conversão e Função de Agregação
# CONVERTENDO VALORES PARA MILHÕES
df.rename(columns={ 'IMPOSTO SOBRE IMPORTAÇÃO': 'Importacao'}, inplace=True)

#Função de String
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

df.to_csv('df_agrupado.csv', sep=';', index=False)

print(f'Arquivo {output_file_key04} enviado para o bucket {bucket_name} com sucesso!')

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

df.to_csv('df_final.csv', sep=';', index=False)

print(f'Arquivo {output_file_key05} enviado para o bucket {bucket_name} com sucesso!')

print(f'Upload de DataFrames para o bucket {bucket_name} concluído com sucesso!')
