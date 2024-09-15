# **Sprint 2 - SQL e Modelagem de Dados Relacionais e Banco de Dados**

## **Sobre o Desafio:**

O objetivo dessa Sprint era a pratica do sql e a modelagem de um bando de dados de uma concessionaria, fazendo a normalização e o dimensionamento desse banco de dados.

## **Etapas**

**1. Modelo Relacional** 

**Codigo fonte Modelo Relacional**

![cliente](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-01-41.png)


![vendedor](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-01-59.png)

![carro_combustivel](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-02-18.png)

![fatoinicial](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-02-35.png)


 **2. Modelo Dimensional**
 
 **Codigo Fonte Modelo Dimensional**

![endereco_cliente](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-01-15.png)

![endereco_locacao](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-02-54.png)

 ![tempo](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-03-36.png)

 
**Explicação dos processos** 

**Normalização**

Seguindo as regras de normalização para minimizar redundancias para garantir a integridade e eficencias do banco de dados. Foi abordado as formas 1NF, 2NF, 3NF para a normalização.
Dos dados disponilizidados no banco de dados "tb_locacao" foram extraidos as seguintes tabelas  "tb_cliente" , "tb_vendedor", "tb_carro", "tb_combustivel" e "tb_fato_locacao" , cada uma dessas contenho id integer proprio como primary key , criando chaves que ligam umas com as outras, dependendo do relacionamento como : one-to-one entre o id_carro com o id_fato_locacao, one-to-one entre id_vendedor com id_locacao, one-to-one id_cliente com id_locacao . Concluise que por id de locacao temos : um cliente, um vendedor, e um carro .
 Tambem temos a relação de many-to-one entre combustivel e carro, ou seja, um carro aceita varias combustiveis. 

 Os dados extraido do banco de dados tb_locacao foram editados para simplificar e criar uma ocorrencia por vez ,e a padronização deste para tabelas pragmaticas.
 
 **Exemplo :**

![cliente](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-01-41.png)

**Relação Dimensional**

Para a fazer o dimensionamento dos dados houve alteração na tabela tb_fato_locacao, com a retirada das columas data_locacao, hora_locacao, data_entrega e hora_entrega ,estes dados sendo remanezados e normalizados em uma nova tabela chamada de tb_locacao_tempo, fazendo assim duas foreign key de tempo de locacao e entrega, criando a dimensao tempo do fato gerador , dividindo-a em dia, mes, ano , dia da semana, assim , facilitando as buscas mais especificas.

**Exemplo:**

![novofato](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-03-36.png)

Foi extraido tambem a dimensao por localização com a tabela endereco_locacao com propria primary key, com uma ocorrencia por endereço , ligada ao id_cliente ,para criar a rela;ao endere;o e cliente(relacao one-to-many) foi criada uma outra tabela endereco_cliente onde  tb_cliente onde fazia a ligacao com uma primary key composta com o id_endereco (id_cliente e id_endereco), podendo agora ter destrinchar os dados por , cidade, estado e pais onde ocorreu a locacao do veiculo, pelo endereço do cliente. 

**Exemplo:**

![endereco_cliente](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2022-03-08.png)


**ERD**
Depois da normazilacao e dimensionamento do banco de dados, assim que ficou o ERD 

![ERD](https://github.com/biancalls/BiancaLages/blob/main/Sprint_2/Evidencias/Screenshot%20from%202024-09-14%2023-04-41.png)


