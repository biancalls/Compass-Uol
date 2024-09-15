# **Sprint 2 - SQL e Modelagem de Dados Relacionais e Banco de Dados**

## **Sobre o Desafio:**

O objetivo dessa Sprint era a pratica do sql e a modelagem de um bando de dados de uma concessionaria, fazendo a normalização e o dimensionamento desse banco de dados.

## **Etapas**

**1. Modelo Relacional** 

**Codigo fonte Modelo Relacional**

 '''sql
 CREATE table tb_cliente (
      id_cliente int PRIMARY KEY,
      nomeCliente varchar (20) 
)
CREATE TABLE tb_vendedor (
       id_vendedor int PRIMARY KEY,
       nomeVendedor varchar(25),
       sexoVendedor smallint,
       estadoVendedor varchar(20) 
       )

CREATE table tb_carro (
         id_carro int PRIMARY KEY,
         km_carro int,
         classi_carro varchar(30),
         marca varchar(15),
         modelo varchar(45),
         ano_carro int
)
CREATE TABLE tb_combustivel (
             id_combustivel int PRIMARY KEY, 
             tipo_combustivel varchar(20),
             id_carro int,
             FOREIGN KEY (id_carro) REFERENCES tb_carro(id_carro) 
           )

 CREATE TABLE tb_fato_locacao (
             id_locacao int PRIMARY KEY,
             data_locacao date,
             hora_locacao time,
             id_cliente int,
             id_vendedor int,
             id_carro int,
             qtd_diaria int,
             vlr_diaria decimal,
             data_entrega date,
             hora_entrega time,
             FOREIGN KEY (id_cliente) REFERENCES tb_cliente (id_cliente),
             FOREIGN KEY (id_vendedor) REFERENCES tb_vendedor (id_vendedor),
 )  
 '''  

 **2. Modelo Dimensional**
 
 **Codigo Fonte Modelo Dimensional**

 '''sql
 CREATE TABLE endereco_cliente (
           id_cliente int,
           id_endereco int,
           PRIMARY KEY (id_cliente, id_endereco),
           FOREIGN KEY (id_cliente) references tb_cliente(id_cliente),
           FOREIGN KEY (id_endereco) REFERENCES tb_endereco(id_endereco))
CREATE TABLE endereco_locacao (
           id_endereco int PRIMARY KEY,
           cidade varchar,
           estado varchar,
           pais varchar 
            )
 CREATE TABLE tb_locacao_tempo (
     id_tempo int IDENTITY(1,1) PRIMARY KEY,
     datacao date,
     hora time,
     dia int,
     mes int,
     ano int,
     dia_da_semana int,
     dia_da_semana_nome varchar(20), 
)
alter table tb_fato_locacao
drop COLUMN data_locacao;
drop COLUMN hora_locacao;
drop COLUMN data_entrega;
drop column hora_entrega
alter table tb_fato_locacao
add fk_tempo_locacao int;
add fk_tempo_entrega int;
ADD CONSTRAINT fk_tempo_locacao_tb_locacao_tempo FOREIGN KEY (fk_tempo_locacao) REFERENCES tb_locacao_tempo(id_tempo);
ADD CONSTRAINT fk_tempo_entrega_tb_locacao_tempo FOREIGN KEY (fk_tempo_entrega) REFERENCES tb_locacao_tempo(id_tempo)
CREATE INDEX idx_tb_locacao_tempo_data ON tb_locacao_tempo(datacao)
'''

**Explicação dos processos** 

**Normalização**

Seguindo as regras de normalização para minimizar redundancias para garantir a integridade e eficencias do banco de dados. Foi abordado as formas 1NF, 2NF, 3NF para a normalização.
Dos dados disponilizidados no banco de dados "tb_locacao" foram extraidos as seguintes tabelas  "tb_cliente" , "tb_vendedor", "tb_carro", "tb_combustivel" e "tb_fato_locacao" , cada uma dessas contenho id integer proprio como primary key , criando chaves que ligam umas com as outras, dependendo do relacionamento como : one-to-one entre o id_carro com o id_fato_locacao, one-to-one entre id_vendedor com id_locacao, one-to-one id_cliente com id_locacao . Concluise que por id de locacao temos : um cliente, um vendedor, e um carro .
 Tambem temos a relação de many-to-one entre combustivel e carro, ou seja, um carro aceita varias combustiveis. 

 Os dados extraido do banco de dados tb_locacao foram editados para simplificar e criar uma ocorrencia por vez ,e a padronização deste para tabelas pragmaticas.
 
 ***Exemplo :**

 ''' sql
 INSERT INTO tb_combustivel (id_combustivel, tipo_combustivel, id_carro)
VALUES
('1','Gasolina','98'),
('2','Gasolina','99'),
('3','Gasolina','3'),
('4','Gasolina','10'),
('5','Gasolina','7'),
('6','Gasolina','6'),
('7','Etanol','2'),
('8','Etanol','4'),
('9','Flex','1'),
('10','Diesel','5') 
'''

**Relação Dimensional**

Para a fazer o dimensionamento dos dados houve alteração na tabela tb_fato_locacao, com a retirada das columas data_locacao, hora_locacao, data_entrega e hora_entrega ,estes dados sendo remanezados e normalizados em uma nova tabela chamada de tb_locacao_tempo, fazendo assim duas foreign key de tempo de locacao e entrega, criando a dimensao tempo do fato gerador , dividindo-a em dia, mes, ano , dia da semana, assim , facilitando as buscas mais especificas.

**Exemplo:**

'''sql
alter table tb_fato_locacao
drop COLUMN data_locacao;
drop COLUMN hora_locacao;
drop COLUMN data_entrega;
drop column hora_entrega

alter table tb_fato_locacao
add fk_tempo_locacao int;
add fk_tempo_entrega int;
ADD CONSTRAINT fk_tempo_locacao_tb_locacao_tempo FOREIGN KEY (fk_tempo_locacao) REFERENCES tb_locacao_tempo(id_tempo);
ADD CONSTRAINT fk_tempo_entrega_tb_locacao_tempo FOREIGN KEY (fk_tempo_entrega) REFERENCES tb_locacao_tempo(id_tempo)
'''

Foi extraido tambem a dimensao por localização com a tabela endereco_locacao com propria primary key, com uma ocorrencia por endereço , ligada ao id_cliente ,para criar a rela;ao endere;o e cliente(relacao one-to-many) foi criada uma outra tabela endereco_cliente onde  tb_cliente onde fazia a ligacao com uma primary key composta com o id_endereco (id_cliente e id_endereco), podendo agora ter destrinchar os dados por , cidade, estado e pais onde ocorreu a locacao do veiculo, pelo endereço do cliente. 

**Exemplo:**

'''sql
CREATE TABLE endereco_cliente (
           id_cliente int,
           id_endereco int,
           PRIMARY KEY (id_cliente, id_endereco),
           FOREIGN KEY (id_cliente) references tb_cliente(id_cliente),
           FOREIGN KEY (id_endereco) REFERENCES tb_endereco(id_endereco)
) 
'''



