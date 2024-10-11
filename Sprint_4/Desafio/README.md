# **Sprint 4 - Docker, Kurbertentes e Linguagem Python**

## **Sobre o Desafio:**

O objetivo do desafio dessa sprint era a prática combinada de Docker com a criação de imagens e containers com scripts Python. Usei o programa Pycharm para realizar o desafio.

## **Etapas**

### **1. Criação de Imagem e Execução de Container** 

**Dockerfile e Diretório execução imagens carguru**

Foi usado Python 3.9-slim para criar uma imagem que não comprometesse demasiadamento a memória do arquivo.

![diretorio_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/criacao_diretorio_carguru.png)

**Processamento Imagem Carguru**


![imagem_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/criacao_imagem_carguru.png)

**Processamento Containers Carguru**

![process_container_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/container_carguru.png)

**Resultado Imagem Carguru**

![resultado_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/resultado_imagem_carguru.png)

**Docker Descktop Imagem**

![docker_imagem_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_carguru_imagem.png)

**Docker Descktop Container**

![docker_container_carguru](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_container_carguru.png)

### **2. Restart Container**

Foi pedido para reiniciar um container existente, a seguir temos o comando restart do container carguru 

![restart_container](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/restart_container.png)

### **3. Criação de novo Script Python , Imagem e Container Docker**

Foi pedido a criação de um script pyhton chamado mascara_dados, esse codigo recebia um input, gerava o hash usando algoritmo SHA-1, imprimindo-o usando método hexdigest , encriptando a string e a mostrando no terminal ,seguentimente retornando ao comando input pedindo outra string, até o comando "ctrl+C" ser inserido pelo usuário, encerrando o loop.

```python
import hashlib

def main():
    while True:
        string = input('Digite algo: ')
        sha1 = hashlib.sha1(string.encode('utf-8')).hexdigest()
        print(f'SHA-1: {sha1}')

if __name__ == '__main__':
    main()

```
![cod_mascara](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/mascara_dados_cod.png)

**Dockerfile e Dirétorio de execução**

![diretorio_mascara](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/mascara_criacao_diretorio.png)

**Build Imagem Mascara Dados**

![process_imagem_mascara](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/process_imagem_mascara.png)

**Criação Container Mascara Dados**

![container_mascara](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/process_containers_mascara.png)

**Renomeação e Resultado Imagem**

![rename](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/process_cod_mascara.png)

**Docker Descktop Imagem**

![docker_imagens](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_imagem_mascara.png)

**Docker Descktop Container**

![docker_containers](https://github.com/biancalls/BiancaLages/blob/main/Sprint_4/Evidencias/Desafio/docker_containers.png)


## **Dificuldades**

As dificuldade que tive nesse desafio foi a criação do script python, tive que fazer uma pesquisa sobre hexdigest e algoritmo SHA-1, para poder concluir o script pedido na etapa 3, sobre encriptação e a importância desta no armazenamanto de dados sensíveis. 





