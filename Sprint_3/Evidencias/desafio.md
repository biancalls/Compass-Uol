```python
#removendo duplicata
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\bianc\\PycharmProjects\\pythonProject\\desafio\\googleplaystore.csv")

df = df.drop_duplicates()
#mostrar as primerias linhas
df.head()
```


```python
#grafico de barra op 5 apps por n° de instalação

df['Installs'] = df['Installs'].str.replace(',', '',regex=False).str.replace('+', '',regex=False).astype(str)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

#agrupando o numero de instalação por app
group_df = df.groupby('App')['Installs'].sum().reset_index()

#colocando em ordem decrescente
sorted_df = group_df.sort_values(by='Installs', ascending=False)

#analisando os 5 primerios app
top_5_apps = sorted_df.head(5)

#gráfio de barras
plt.figure(figsize=(10, 6))
plt.bar(top_5_apps['App'], top_5_apps['Installs'])
plt.xlabel('App')
plt.ylabel('Installs')
plt.title('Top 5 Apps')
plt.xticks(rotation=45)
plt.grid(axis='x')
plt.show()
```


```python
#pegando as categorias do app
category_cont = df['Category'].value_counts()
#gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(category_cont, labels=category_cont.index, autopct='%1.1f%%',startangle=140)
plt.title('App Categories')
plt.show()
```


```python

#cenvertendo a coluna price para float, tratando erros
def conversor(preço):
     try:
         if isinstance(preço,str):
            return float(preço.replace('$', '').strip())
         else:
            return float(preço)
     except ValueError:
         return np.nan

df['Price'] = df['Price'].apply(conversor)

#filtra somente os app pagos (apos tratamento de dados)
app_pagos = df[df['Price'] != 0]
#verifica se há valores nan e os remove 
if app_pagos['Price'].isna().any():
    app_pagos = app_pagos.dropna(subset=['Price'])
#Seleciona o app mais caro entre os pagos ignora
app_mais_caro = app_pagos.loc[app_pagos['Price'].idxmax(skipna=True)]
print(f'O app mais caro é {app_mais_caro['App']} e custa R${app_mais_caro["Price"]:.2f}')
```


```python
#contagem dos app classificados como Matur 17+
mature_apps = df[df['Content Rating'] == 'Mature 17+'].shape[0]
print('Número de apps Mature 17+:', mature_apps)
```


```python
#ordena os app por numero de reviews de forma decrescente
top_apps_reviews = df.sort_values(by='Reviews', ascending=False)
#seleciona os 10 maiores apps
top_10_apps = top_apps_reviews.head(10)
#criação da lista
top_10_lista = [(app,reviews) for app,reviews in zip(top_10_apps['App'],top_10_apps['Reviews'])]
#resultado lista
print('Top 10 Apps por Reviews:')
for app, reviews in top_10_lista:
    print(f'{app}: {reviews}')
```


```python
# contagem da quantidade de app gratiutos do dataset
free_apps = df[df['Price'] == 0 ].shape[0]
print('Número de apps gratuitos:', free_apps)
```


```python
#ordenando os app por ordem crescente
pior_rating_app = df.sort_values(by='Rating', ascending=True)
#seleciona os 10 com menor rating
dez_piores = pior_rating_app.head(10)
#cria uma lista
lista_10_piores = [(app,rating) for app, rating in zip(dez_piores['App'], dez_piores['Rating'])]
#resultado
print('10 Apps com menor rating:')
for app,rating in lista_10_piores:
    print(f'{app}: {rating}')
```


```python
#ordena os app por n° de reviews
top_apps_reviews = df.sort_values(by='Reviews', ascending=False)
#seleciona os 10 maiores app
top_10_apps = top_apps_reviews.head(10)
#grafico de barras horizontais
plt.figure(figsize=(10,6))
plt.barh(top_10_apps['App'], top_10_apps['Reviews'])
plt.xlabel('App')
plt.ylabel('Reviews')
plt.title('Top 10 Apps')
plt.xticks(rotation=45, ha='right')
plt.gca().invert_yaxis() 
plt.grid(axis='x')
plt.show()
```


```python
#filtro dos app pagos
app_pagos = df[df['Price'] != 0]

#criando histograma
plt.hist(app_pagos['Reviews'], bins=10, color = 'orange', edgecolor='black')
plt.xscale('log')
plt.xlabel('Reviews')
plt.ylabel('Frequências')
plt.title('Distribuição de Reviews dos Aplicativos Pagos')
plt.show()

```
