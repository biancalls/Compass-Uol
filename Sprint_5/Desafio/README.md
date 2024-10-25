# **Sprint 5 - Computação em nuvem e Sistema AWS**

## **Sobre o Desafio:**

O objetivo do desafio dessa sprint era a prática dos conhecimentos de AWS. Usei o programa Pycharm para realizar o desafio.

## **Etapas**

### **ARQUIVO CSV NO PORTAL DE DADOS PÚBLICOS DO GOVERNO BRASILEIRO**

Escolhi os dados de arrecadação de impostos por estado referente aos anos 2000 ate agosto de 2024. Nesse arquivo csv denominado arrecadacao-estado.csv , possui as arrecadação por impostos por estado 'UF' por mês, como impostos sobre importação , ipi sobre automoveis entre outros. Sou formada em Ciências Contábeis e escolhi um csv que com esses conhecimentos da graduação eu conseguiria interpretar com mas facilidade os dados.

![arredacacao-estado.csv](../Sprint_5/Desafio/arrecadacao-estado.csv)

### **CRIAÇÃO BUCKET USANDO SCRIPT PYTHON E BIBLIOTECA BOTO3**

**Criando o bucket por script Python usando boto3 e o upload do arquivo csv**

```python

import boto3
import os

s3 = session.resource('s3')

bucket = 'biancalages05'

s3.create_bucket(Bucket=bucket)

arquivo= 'C:\\Users\\bianc\\PycharmProjects\\pythonProject\\aws_desafio\\arrecadacao-estado.csv'

nome_arquivo = 'arrecadacao-estado.csv'

s3.Bucket(bucket).upload_file(arquivo, nome_arquivo)


print(f'Arquivo {nome_arquivo} enviado para o bicket {bucket} com sucesso!')

```

**UPLOAD ARQUIVO CSV ARRECADAÇÃO-ESTADO.CSV PARA O BUCKET BIANCALAGES05**

![UPLOADCSVORG](../Sprint_5/Evidências/Desafio/UPLOADCSVORG.png)

**Bucket nos console AWS**

![BUCKETAWS](../Sprint_5/Evidências/Desafio/BUCKETAWS.png)

![CONECTAWS](../Sprint_5/Evidências/Desafio/CONECTAWS.png)

### **CRIAÇÃO DATAFRAME COM PANDAS E AS MANIPULAÇÕES DO DATAFRAME**

**Filtro com dois operadores lógicos**

```python
import pandas as pd

df = pd.read_csv('/Sprint_5/Desafio/Arquivos_csv/arrecadacao-estado.csv', delimiter=';', encoding='latin1')
numeric_cols = df.columns[3:]  # Seleciona as colunas a partir da terceira
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
# Renomear colunas
df.rename(columns={'IPI - AUTOMÓVEIS': 'IPI_Automoveis'}, inplace=True)
df['IPI_Automoveis'] = pd.to_numeric(df['IPI_Automoveis'], errors='coerce')
df['IPI - VINCULADO À IMPORTACAO'] = pd.to_numeric(df['IPI - VINCULADO À IMPORTACAO'], errors='coerce')

# ESTADOS COM ARRECADAÇÃO DE IPI- AUTOMÓVEIS ACIMA DE 10 MILHÕES E IPI- VINCULADO À IMPORTAÇÃO ACIMA DE 5 MILHÕES
filtro = (df['IPI_Automoveis'] > 10000000) & (df['IPI - VINCULADO À IMPORTACAO'] > 5000000)
df_filtrados = df[filtro]

```

A manipulução do arquivo começa com essa parte do script python temos a criação do dataframe (df) a partir dos dados do arquivo csv , indicando que os dado são separados por (;) e especificando as codificação dos caracteres do arquivo em lantin1, pois essa codificação lida com caracteres epeciais como acentos e (ç) presentes no dataframe. Depois a conversão dos dados a partir da 3º coluna em float. Renomeamos uma coluna especifica IPI - AUTOMÓVEIS em IPI_Automoveis e transformando os dados desta e da tabela IPI - VINCULADA Â IMPORTAÇÃO em números, garantindo que os dados sejam tratados como números. Foi feito um um filtro lógico para selecionar as linhas onde o valor de 'IPI_Automoveis' é maior que 10.000.000 e o valor de 'IPI - VINCULADO À IMPORTACAO' é maior que 5.000.000.  

![DF_FILTRADO](../Sprint_5/Evidências/Desafio/DF_FILTRADO.png)

**Função de agregação**

```python
# AGRUPA POR ESTADO E SOMA A IMPORTAÇÃO
df['IMPOSTO SOBRE IMPORTAÇÃO'] = pd.to_numeric(df['IMPOSTO SOBRE IMPORTAÇÃO'], errors='coerce')

agregado = df.groupby('UF')['IMPOSTO SOBRE IMPORTAÇÃO'].sum()

```

Nesta parte do script seleciona a coluna IMPOSTO SOBRE IMPORTAÇÃO e a converte em numeric e se houver valores que não possam ser convertidos para números , serão convertidos para NaN. Agrupando os dados por 'UF' e calcula a soma dos valores da coluna IMPOSTO SOBRE IMPORTAÇÃO para cada estado.

![DF_AGREGADO](../Sprint_5/Evidências/Desafio/DF_AGREGADO.png)

**Função Condicional**

```python
# ESTADOS COM ARRECADAÇÃO DE IRPF É MAIOR QUE IRPJ
def arrecadacao_IRPF_IRPJ(df):
    return df[df['IRPF'] > df['IRPJ - DEMAIS EMPRESAS']]

df_IRPF_maior_IRPJ = arrecadacao_IRPF_IRPJ(df)
```

Essa parte do script apresenta os estados onde o IRPF (Imposto de Renda Pessoa Física) é maior do que a arrecadação do IRPJ (Imposto de Renda Pessoa Jurídica).

![DF_IRPF_IRPJ](../Sprint_5/Evidências/Desafio/DF_IRPF_IRPJ.png)

**Função de conversão e Função de Agregação**
```python
# CONVERTENDO VALORES PARA MILHÕES
df.rename(columns={ 'IMPOSTO SOBRE IMPORTAÇÃO': 'Importacao'}, inplace=True)

def converter_milhoes(valor):
    return valor / 1000000

df['Importação_milhoes'] = df['Importacao'].apply(converter_milhoes)


# ANÁLISE ANUAL por UF POR IMPORTAÇÃO
def ano_UF(df, coluna_valor):
    df_agrupado = df.groupby(['Ano', 'UF'])[coluna_valor].sum().reset_index()
    return df_agrupado

df_agrupado = ano_UF(df, 'Importacao')
```

De acordo com o script a seguir temos a renomeação da coluna 'IMPOSTO SOBRE IMPORTAÇÃO' para 'Importacao' para simplificar o código e melhorar a legibilidade. Temos a conversão com uma função chamada converter_milhoes os dads da coluna Importacao em aumentando a legibilidade dos dados. Temos outra função que soma por ano e estados os dados do dataframe, neste caso a coluna 'Importacao'.  

![DF_AGRUPADO](../Sprint_5/Evidências/Desafio/DF_AGRUPADO.png)

**Função de String**

```python
def converter_mes_para_maiusculas(df):
    df['Mês'] = df['Mês'].str.upper()
    return df

df = converter_mes_para_maiusculas(df)
```

Aqui temos uma função que converte os dados na coluna MÊS em upper e depois aplicada a função no dataframe criado.

![DF_FINAL](../Sprint_5/Evidências/Desafio/DF_FINAL.png)

## **UPLOAD PARA O BUCKET S3 USANDO BOTO3**

![CRIACAOOBEJECTUCKET](../Sprint_5/Evidências/Desafio/CRIACAOOBJECTBUCKET.png)

![OBJECTSBUCKET](../Sprint_5/Evidências/Desafio/OBJECTSBUCKET.png)

## **Dificuldades**

As dificuldade que tive nesse desafio foi as questões de dificuldade com a connectividade da AWS com Pycharm , teve que colocar as chaves de acesso dentro do código python para conseguir fazer o upload dos arquivos csv para o bucket dentro do S3. Com a ajuda da minha SQUAD e dos pessoa da minha turma tive sucesso na execução do desafio. 





