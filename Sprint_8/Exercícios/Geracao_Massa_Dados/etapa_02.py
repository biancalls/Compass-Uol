import random

animais = ['cachorro','gato','elefante','girafa','leão','tigre','macaco','panda','coelho','rato'
           'cavalo','vaca','ovelha','porco','galinha','pato','peixe','pássaro','cabra','jacaré']

random.shuffle(animais)
animais.sort()
for animal in animais:
    print(animal)

with open('animais.csv','w') as arquivos:
    for animal in animais:
        arquivos.write(f'{animal}\n')