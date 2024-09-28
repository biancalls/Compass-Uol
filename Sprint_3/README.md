# **Sprint 3 - A linguagem Python**

## **O que foi feito nessa Sprint 2?**

 Nessa Sprint 3 tivemos a introdução da linguagem pyhton, sua sintaxe e características que a tornam tão aderente ao processamento de dados.


## **Exercicios**

Os exercícios dessa sprint foram os sequintes scripts usando o pyhton.

**01.**

```python
def calcular_100(nome,idade_att):
    import datetime
    ano = datetime.datetime.now().year
    idade_100 = 100 - idade_att
    ano_100 = ano + idade_100
    print(f'{ano_100}')
    
nome = 'Bianca'
idade = int('28')
calcular_100(nome,idade)
```

**02.**

```python
numeros = list(range(2,5))
for numero in numeros:
    if numero % 2 ==0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')
```

**03.**

```python
for numeros in range(0,21,2):
    print(f'{numeros}')
```

**04.**

```python
def primos(numeros):
    if numeros <= 1:
        return False
    if numeros <= 3:
        return True
    if numeros % 2 == 0 or numeros % 3 == 0:
        return False
    i = 5
    while i * i <= numeros:
        if numeros % i == 0 or numeros % (i+2) == 0:
            return False
        i += 6
    return True
        
for numeros in range(1,101):
    if primos(numeros):
        print(numeros)
```

**05.**

```python
dia = int(22)
mes = int(10)
ano = int(2022)
print(f'{dia}/{mes}/{ano}')
```

**06.**

```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_a = set(a)
lista_b = set(b)
comun = lista_a.intersection(lista_b)
intersecao = list(comun)
print(intersecao)
```

**07.**

```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = list()
for numeros in a:
    if numeros % 2 != 0:
        impares.append(numeros)
        
print(impares)
```

**08.**

```python
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
```

**09.**

```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
for indice, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{indice} - {primeirosNomes} {sobreNomes} está com {idades} anos')
```

**10.**

```python
def sem_duplicadas(lista):
    return list(set(lista))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_a = sem_duplicadas(lista)
print(lista_a)
```

**11.**

```python
import json
with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)
print(dados)
```

**12.**

```python
def my_map(lista,f):
    resultado = []
    for n in lista:
        resultado.append(f(n))
    return resultado


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadrado(x):
    return x**2


resultado = my_map(numeros,quadrado)
print(resultado)
```

**13.**

```python
def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo, end = '')
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado')
        
abrir_arquivo("arquivo_texto.txt")
```

**14.**

```python
def imp_parametros(*par1, **par2):
    for n in par1:
        print(str(n).strip())
    
    for c,v in par2.items():
        print(f"{v}")
        
imp_parametros(1,3,4,'hello', parametro_nomeado ='alguma coisa',x = 20)
```

**15.**

```python
class Lampada:
    def __init__(self, estado):
        self.ligada = estado
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada
        
lampada = Lampada(False)

lampada.liga()

print('A lâmpada está ligada?', lampada.esta_ligada())

lampada.desliga()

print('A lâmpada ainda está ligada?', lampada.esta_ligada())

```

**16.**

```python
def soma(str_num):
    numeros = str_num.split(',')
    soma = 0
    for num in numeros:
        soma += int(num)
    return soma
    
str_num = "1,3,4,6,10,76"
resposta = soma(str_num)
print(resposta)
```

**17.**

```python
def div_lista(lista):
    tamanho = len(lista)
    divisao = tamanho // 3
    p1 = lista[:divisao]
    p2 = lista[divisao:divisao*2]
    p3 = lista[divisao*2:]
    return p1, p2, p3
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

p1, p2, p3 = div_lista(lista)

print(p1, end=' ')
print(p2,end=' ')
print(p3)

```

**18.**

```python
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

dados = set(speed.values())
nova_lista = list(dados)
print(nova_lista)

```

**19.**

```python
import random

random_list = random.sample(range(500), 50)
random_list.sort()

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

if len(random_list) % 2 == 0:
    metade = len(random_list) // 2
    mediana = (random_list[metade-1] + random_list[metade]) / 2
else:
    mediana = random_list[len(random_list) // 2]
    
print(f'Media: {media:.2f}', end=', ')
print(f'Mediana: {mediana}', end=', ')
print(f'Mínimo: {valor_minimo}', end=', ')
print(f'Máximo: {valor_maximo}')
```

**20.**

```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
dados = a[::-1]
print(dados)
```

**21.**

```python
class Passaro:
    def voar(self):
        print('Voando...')
        
    def som(self):
        pass
    
class Pato(Passaro):
    def som(self):
        print('\nPato emitindo som...')
        print('Quack Quack')
        
class Pardal(Passaro):
    def som(self):
        print('\nPardal emitindo som...')
        print('Piu Piu')
        
pato = Pato()
pardal = Pardal()

print('Pato')
pato.voar()
pato.som()

print('Pardal')
pardal.voar()
pardal.som()

```

**22.**

```python
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None
        
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
```

**23.**

```python
class Calculo:
    def soma(self,x,y):
        return x + y
    
    def menos(self,x,y):
        return x - y
    
dados = Calculo()
x = 4
y = 5

resp_soma = dados.soma(x,y)
resp_menos = dados.menos(x,y)

print(f'Somando: {x}+{y} = {resp_soma}')
print(f'Subtraindo: {x}-{y} = {resp_menos}')
```

**24.**

```python
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
        
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
        
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada
        
crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

resp_cresc = crescente.ordenacaoCrescente()
resp_decres = decrescente.ordenacaoDecrescente()

print(resp_cresc)
print(resp_decres)
```

**25.**

```python
class Aviao:
    def __init__(self,modelo,velocidade_maxima,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"
        
avioes = []

av1 = Aviao('BOIENG456',1500,400)
av2 = Aviao('Embraer Praetor 600',863,14)
av3 = Aviao('Antonov An-2',258,12)

avioes.append(av1)
avioes.append(av2)
avioes.append(av3)

for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.")
```

**Exercicio ETL com Python.**

**1-TRANSFORMANDO DADOS EM UM DICIONÁRIO**

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

**ETAPA 1 - Ator/Atriz com amior númerio de filmes e a quantidade**

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
 **Resultado Etapa 1**
 
 Actor: Robert DeNiro
Total Gross: 3081.30 
Number of Movies: 79
Average per Movie: 39.00 
#1 Movie: Meet the Fockers
Gross: 279.30 

**ETAPA 2 - Média da receita de bilheteria bruta dos principais filmes**

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
 **Resultado Etapa 2**
 
 A media da receita bruta dos principais filmes : 428.69

**ETAPA 3 - Ator/Atriz com a maior média da receita de bilheteria bruta**

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
 **Resultado Etapa 3**
 
 451.8 : Anthony Daniels
 
**ETAPA 4 - O filme (nome filme) aparece (quantidade) vez(es) no dataset**

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
**Resultado Etapa 4**

O filme The Avengers aparece 6 vez(es) no dataset 
O filme Catching Fire aparece 4 vez(es) no dataset 
O filme Harry Potter / Deathly Hallows (P2) aparece 4 vez(es) no dataset 
O filme Star Wars: The Force Awakens aparece 3 vez(es) no dataset 
O filme The Dark Knight aparece 3 vez(es) no dataset 
O filme Meet the Fockers aparece 3 vez(es) no dataset 
O filme Shrek 2 aparece 2 vez(es) no dataset 
O filme Dead Man's Chest aparece 2 vez(es) no dataset 
O filme Night at the Museum aparece 2 vez(es) no dataset 
O filme Return of the King aparece 2 vez(es) no dataset 
O filme Avengers: Age of Ultron aparece 2 vez(es) no dataset 
O filme Toy Story 3 aparece 1 vez(es) no dataset 
O filme War of the Worlds aparece 1 vez(es) no dataset 
O filme Sixth Sense aparece 1 vez(es) no dataset 
O filme Independence Day aparece 1 vez(es) no dataset 
O filme The Martian aparece 1 vez(es) no dataset 
O filme The Phantom Menace aparece 1 vez(es) no dataset 
O filme Ocean's Eleven aparece 1 vez(es) no dataset 
O filme Men in Black aparece 1 vez(es) no dataset 
O filme World War Z aparece 1 vez(es) no dataset 
O filme Hotel Transylvania 2 aparece 1 vez(es) no dataset 
O filme The LEGO Movie aparece 1 vez(es) no dataset 
O filme American Sniper aparece 1 vez(es) no dataset 
O filme Transformers 4 aparece 1 vez(es) no dataset 
O filme The Grinch aparece 1 vez(es) no dataset 
O filme Titanic aparece 1 vez(es) no dataset 
O filme Minions aparece 1 vez(es) no dataset 
O filme The Dark Knight Rises aparece 1 vez(es) no dataset

**ETAPA 5 - Lista dos atores pela receita bruta em ordem decrescente**

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
**Resultado Etapa 5**

Harrison Ford - 4871.70 
Samuel L. Jackson - 4772.80 
Morgan Freeman - 4468.30 
Tom Hanks - 4340.80 
Robert Downey, Jr. - 3947.30 
Eddie Murphy - 3810.40 
Tom Cruise - 3587.20 
Johnny Depp - 3368.60 
Michael Caine - 3351.50 
Scarlett Johansson - 3341.20 
Gary Oldman - 3294.00 
Robin Williams - 3279.30 
Bruce Willis - 3189.40 
Stellan Skarsgard - 3175.00 
Anthony Daniels - 3162.90 
Ian McKellen - 3150.40 
Will Smith - 3149.10 
Stanley Tucci - 3123.90 
Matt Damon - 3107.30 
Robert DeNiro - 3081.30 
Cameron Diaz - 3031.70 
Liam Neeson - 2942.70 
Andy Serkis - 2890.60 
Don Cheadle - 2885.40 
Ben Stiller - 2827.00 
Helena Bonham Carter - 2822.00 
Orlando Bloom - 2815.80 
Woody Harrelson - 2815.80 
Cate Blanchett - 2802.60 
Julia Roberts - 2735.30 
Elizabeth Banks - 2726.30 
Ralph Fiennes - 2715.30 
Emma Watson - 2681.90 
Tommy Lee Jones - 2681.30 
Brad Pitt - 2680.90 
Adam Sandler - 2661.00 
Daniel Radcliffe - 2634.40 
Jonah Hill - 2605.10 
Owen Wilson - 2602.30 
Idris Elba - 2580.60 
Bradley Cooper - 2557.70 
Mark Wahlberg - 2549.80 
Jim Carrey - 2545.20 
Dustin Hoffman - 2522.10 
Leonardo DiCaprio - 2518.30 
Jeremy Renner - 2500.30 
Philip Seymour Hoffman - 2463.70 
Sandra Bullock - 2462.60 
Chris Evans - 2457.80 
Anne Hathaway - 2416.50 

## **Evidências**

[markdown_exercicio](https://github.com/biancalls/BiancaLages/blob/main/Sprint_3/Evidencias/exercicios_sprint3.md)

[markdown_etl](https://github.com/biancalls/BiancaLages/blob/main/Sprint_3/Evidencias/exercicioETL.md)

[markdown_desafio](https://github.com/biancalls/BiancaLages/blob/main/Sprint_3/Evidencias/exercicioETL.md)

## **Dificuldades**

Nessa sprint tive algumas dificuldades tecnicas devido a falta de prática com o pyhton anteriormente, porém com a ajuda do meu SQUAD, da minha turma, pesquisas em forunse youtube consegui resolver os exercícios e o desafio. Tive um certa dificuldade no arquivo csv do desafio, tem um erro na coluna Price , dificultou porem consegui resolver, outro foi a escolha dos gráficos para os dados do dataframe, mas consegui resolver nas melhores das minha habilidade atuais.  

