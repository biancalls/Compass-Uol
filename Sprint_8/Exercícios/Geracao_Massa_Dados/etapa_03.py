import names
import random
import os
import time


random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())
print(f"Gerando {qtd_nomes_aleatorios} nomes aleatorios".format(qtd_nomes_aleatorios))

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

output_file = "nomes_aleatorios.txt"
with open(output_file, "w",encoding='utf-8') as arquivo:
    for nome in dados:
        arquivo.write(nome + '\n')

print(f'Arquivo {output_file} criado com sucesso!')
