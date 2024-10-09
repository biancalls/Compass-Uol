# **Sprint 4 - Docker e Linguagem Python** 

## **O que foi feito nessa Sprint 4?**

Nessa Sprint 4 tivemos a introdução dos Containers Docker e Kubertentes, como também tivemos uma extenção do uso de Python com estatisticas e criação de gráficos, complementando a sprint anterior.  


## **Exercicios**

Os exercicios propostos nessa sprint consistiam em exercícios python high order function.

**01.**

```python
with open ('number.txt','r') as f :
    numeros = [int(num) for num in f.read().split()]
    
numeros = list(map(int,numeros))

pares = list(filter(lambda x: x % 2 == 0, numeros))

ordenados = sorted(pares, reverse=True)

cinco_maiores = ordenados[:5]

soma_pares = sum(cinco_maiores)
    
print(cinco_maiores)
print(soma_pares)
```
![EX01](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex01.png)

**02.**

```python
def conta_vogais(texto:str)-> int:
    vogais = 'aeiou'
    vogais_string = filter(lambda letra: letra.lower() in vogais, texto)
    return len(list(vogais_string))
```

![EX02](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex02.png)

**03.**

```python
from functools import reduce
def calcula_saldo(lancamentos) -> float:
    #continue este código
    def valor_lancamento(lancamentos):
        valor, tipo = lancamentos
        return valor if tipo == 'C' else -valor

    saldo_final = reduce(lambda x,y: x+y, map(valor_lancamento, lancamentos))
    return saldo_final
```

![EX03](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex03.png)

**04.**

```python
def calcular_valor_maximo(operadores,operandos) -> float:
    operacao = lambda op, a, b: a + b if op== '+' else a - b if op == '-' else a * b if op == '*' else a / b if op == '/' else a % b
        

    resultados = list(map(lambda x: operacao(x[0], x[1][0], x[1][1]), zip(operadores,operandos)))
    return max(resultados)


operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))
```

![EX04](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex04.png)

**05.**

```python
import csv

def boletim(arquivo_csv):
    with open(arquivo_csv, 'r') as file:
        estudante = csv.reader(file)
        
        
        dados = []
        for linhas in estudante:
            nome = linhas[0]
            notas = list(map(int, linhas[1:]))
            ordenadas = sorted(notas, reverse=True)[:3]
            media = round(sum(ordenadas) / 3, 2)
            dados.append((nome,ordenadas,media))
    
        estudante_ordenado = sorted(dados, key=lambda x: x[0])
        for nome, notas, media in estudante_ordenado:
            print(f'Nome: {nome} Notas: {notas} Média: {media}')
            
            
boletim('estudantes.csv')
        
```

![EX05](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex05.png)

**06.**

```python
def maiores_que_media(conteudo:dict)->list:
    precos = list(conteudo.values())
    media = sum(precos) / len(precos)
    
    acima_media = [(produto,preço) for produto, preço in conteudo.items() if preço > media]
    ordenados = sorted(acima_media, key=lambda x: x[1])
    
    return ordenados
    
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo)
```
![EX06](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex06.png)

**07.**

```python
def pares_ate(n:int):
    if n < 2:
        return ('Não há numeros pares no intervalo')
    for numero in range(2, n+1 ,2):
        yield numero
````

![EX07](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Exercicios/ex07.png)


## **Desafio**

O desafio dessa sprint consistia no criação de imagens e containers usando Docker. A seguir, temos os containers e imagens resultantes da resolução do desafio.

**Imagens Docker** 

![imagens_docker](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_imagens.png)

**Containers Docker**

![containers_docker](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_containers.png)

## **Certificados AWS**

![Certificado AWS - Credenciamento Técnico (Português)](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Certificados/13246_3_6213879_1728344391_AWS%20Course%20Completion%20Certificate.pdf)

## **Dificuldades**

Essa sprint foi tranquila, tivemos cursos que complementavam os assuntos da sprint anterior e novidades. Docker é um programa bastante utilizado na área de ciências de dados, sendo uma otima ferramenta de se ter um curso detalhado e prática como foi dado nessa sprint.  
