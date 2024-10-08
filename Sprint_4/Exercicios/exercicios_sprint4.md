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


```python
def conta_vogais(texto:str)-> int:
    vogais = 'aeiou'
    vogais_string = filter(lambda letra: letra.lower() in vogais, texto)
    return len(list(vogais_string))
```


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


```python
def calcular_valor_maximo(operadores,operandos) -> float:
    operacao = lambda op, a, b: a + b if op== '+' else a - b if op == '-' else a * b if op == '*' else a / b if op == '/' else a % b
        

    resultados = list(map(lambda x: operacao(x[0], x[1][0], x[1][1]), zip(operadores,operandos)))
    return max(resultados)


operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))
```


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


```python
def pares_ate(n:int):
    if n < 2:
        return ('Não há numeros pares no intervalo')
    for numero in range(2, n+1 ,2):
        yield numero
        
            
```


```python

```
