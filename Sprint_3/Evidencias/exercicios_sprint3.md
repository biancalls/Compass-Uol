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


```python
numeros = list(range(2,5))
for numero in numeros:
    if numero % 2 ==0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')
```


```python
for numeros in range(0,21,2):
    print(f'{numeros}')
```


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


```python
dia = int(22)
mes = int(10)
ano = int(2022)
print(f'{dia}/{mes}/{ano}')
```


```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_a = set(a)
lista_b = set(b)
comun = lista_a.intersection(lista_b)
intersecao = list(comun)
print(intersecao)
```


```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = list()
for numeros in a:
    if numeros % 2 != 0:
        impares.append(numeros)
        
print(impares)
```


```python
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
```


```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
for indice, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{indice} - {primeirosNomes} {sobreNomes} está com {idades} anos')
```


```python
def sem_duplicadas(lista):
    return list(set(lista))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_a = sem_duplicadas(lista)
print(lista_a)
```


```python
import json
with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)
print(dados)
```


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


```python
def imp_parametros(*par1, **par2):
    for n in par1:
        print(str(n).strip())
    
    for c,v in par2.items():
        print(f"{v}")
        
imp_parametros(1,3,4,'hello', parametro_nomeado ='alguma coisa',x = 20)
```


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


```python
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

dados = set(speed.values())
nova_lista = list(dados)
print(nova_lista)

```


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


```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
dados = a[::-1]
print(dados)
```


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
















