```python
import csv
from collections import Counter
def dic_atores(dados_csv):
    dados_csv = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\actors.csv"
    atores = {}
    with open(dados_csv, 'r') as arquivo:
        reader = csv.reader(arquivo)
        header = next(reader)
        for linhas in reader:
            ator = {}
            for chave, valor in zip(header, linhas):
                ator[chave] = valor
            atores[ator['Actor']] = ator
    return atores

hollywood = dic_atores("C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_1.txt")
```


```python
def maior_numerodefilmes(atores, dados_txt):
    dados_txt = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_1.txt"
    ator_maior = max(atores, key=lambda ator: int(atores[ator]['Number of Movies']))
    dados_ator = atores[ator_maior]

    with open(dados_txt,'w') as saida:
        for chave, valor in dados_ator.items():
            saida.write(f"{chave}: {valor}\n")

maior_numerodefilmes(hollywood , "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_1.txt")
```


```python
def contador_mediagross(atores):
    total_receita = 0
    num_filmes = 0
    for ator in atores.values():
        total_receita += float(ator['Gross'])
        num_filmes += 1
    media = total_receita / num_filmes
    return round(media, 2)

def media_gross(atores, dados2_txt):
    dados2_txt = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_2.txt"

    with open(dados2_txt, 'w') as arquivo2:
        arquivo2.write(f'A media da receita bruta dos principais filmes : {media:.2f}')

media = contador_mediagross(hollywood)
media_gross(media,"C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_2.txt")
```


```python
def media_average(atores,chave):
    maior_valor = None
    ator_maior = None
    for ator, dados in atores.items():
        valor = float(dados['Average per Movie'])
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            ator_maior = ator
    return ator_maior, maior_valor

maior_valor, ator_maior = media_average(hollywood,"Average per Movie")


dados3_txt = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_3.txt"
with open(dados3_txt, 'w') as arquivo3:
       arquivo3.write(f'{ator_maior} : {maior_valor}')
```


```python
def cont_movie(hollywood):
    contagem_filmes = Counter()
    for ator in hollywood.values():
        contagem_filmes[ator['#1 Movie']] += 1
    return contagem_filmes

def resultado(contagem_filmes,dados4_txt):
    dados4_txt = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_4.txt"
    with open (dados4_txt,'w') as arquivo4:
        for filme, aparicoes in contagem_filmes.most_common():
            arquivo4.write(f'O filme {filme} aparece {aparicoes} vez(es) no dataset \n')

contagem_filmes = cont_movie(hollywood)
resultado(contagem_filmes,"C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_4.txt")

```


```python
def ator_por_receita(hollywood):
    atores_ordem = sorted(hollywood.items(), key=lambda x: float(x[1]['Total Gross']), reverse=True)
    return atores_ordem

def resultado(atores_ordem,dados5_txt):
    dados5_txt = "C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_5.txt"
    with open (dados5_txt,'w') as arquivo5:
        for ator, dados in atores_ordem:
            arquivo5.write(f'{ator} - {dados['Total Gross']}\n')

atores_ordem = ator_por_receita(hollywood)
resultado(atores_ordem,"C:\\Users\\bianc\\PycharmProjects\\pythonProject\\exercicioETL\\etapa_5.txt")
```


```python

```
