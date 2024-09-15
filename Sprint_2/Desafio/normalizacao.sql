

CREATE table tb_cliente (
      id_cliente int PRIMARY KEY,
      nomeCliente varchar (20) 
)

values
('2', 'Cliente dois'),
('3', 'Cliente tres'),
('4', 'Cliente quatro'),
('5',  'Cliente cinco'),
('6', 'Cliente seis'),
('10', 'Cliente dez'),
('20', 'Cliente vinte'),
('22', 'Cliente vinte e dois'),
('23', 'Cliente vinte e tres'),
('26', 'Cliente vinte e seis')




CREATE TABLE tb_vendedor (
       id_vendedor int PRIMARY KEY,
       nomeVendedor varchar(25),
       sexoVendedor smallint,
       estadoVendedor varchar(20) 
       )
           

INSERT INTO tb_vendedor (id_vendedor, nome_vendedor, sexo_vendedor, estado_vendedor)
VALUES
('5', 'Vendedor 5', '0', 'SP'),
('6', 'Vendedor 6', '1', 'SP'),
('7', 'Vendedor 7', '1', 'RJ'),
('8', 'Vendedor 8', '1', 'MG'),
('16', 'Vendedor 16', '0', 'AM'),
('30', 'Vendedor 30', '0', 'RS'),
('31', 'Vendedor 31', '0', 'CE'),
('32', 'Vendedor 32', '1', 'MS')



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
             FOREIGN KEY (id_carro) REFERENCES tb_carro (id_carro)
                       )                    
             
INSERT INTO tb_fato_locacao 
(id_locacao, data_locacao, hora_locacao , id_cliente , id_vendedor , id_carro ,qtd_diaria , vlr_diaria ,data_entrega ,hora_entrega)
VALUES
('1',"2015-01-10","10:00",'2','5','98','2','100',"2015-01-12","10:00"),
('2',"2015-02-10","12:00",'2','5','98','2','100',"2015-02-12","12:00"),
('3',"2015-02-13","12:00",'3','6','99','2','150',"2015-02-15","12:00"),
('4',"2015-02-15","13:00",'4','6','99','5','150',"2015-02-20","13:00"),
('5',"2015-03-02","14:00",'4','7','99','5','150',"2015-03-07","14:00"),
('6',"2016-03-02","14:00",'6','8','3','10','250',"2016-03-12","14:00"),
('7',"2016-08-02","14:00",'6','8','3','10','250',"2016-08-12","14:00"),
('8',"2017-01-02","18:00",'4','6','3','10','250',"2017-01-12","18:00"),
('9',"2018-01-02","18:00",'4','6','3','10','280',"2018-01-12","18:00"),
('10',"2018-03-02","18:00",'10','16','10','10','50',"2018-03-12","18:00"),
('11',"2018-04-01","11:00",'20','16','7','10','50',"2018-04-11","11:00"),
('12',"2020-04-01","11:00",'20','16','6','10','150',"2020-04-11","11:00"),
('13',"2022-05-01","8:00",'22','30','2','20','150',"2022-05-21","18:00"),
('14',"2022-06-01","8:00",'22','30','2','20','150',"2022-06-21","18:00"),
('15',"2022-07-01","8:00",'22','30','2','20','150',"2022-07-21","18:00"),
('16',"2022-08-01","8:00",'22','30','2','20','150',"2022-07-21","18:00"),
('17',"2022-09-01","8:00",'23','31','4','20','150',"2022-09-21","18:00"),
('18',"2022-10-01","8:00",'23','31','4','20','150',"2022-10-21","18:00"),
('19',"2022-11-01","8:00",'23','31','4','20','150',"2022-11-21","18:00"),
('20',"2023-01-02","18:00",'5','16','1','10','880',"2023-01-12","18:00"),
('21',"2023-01-15","18:00",'5','16','1','10','880',"2023-01-25","18:00"),
('22',"2023-01-25","8:00",'26','32','5','5','600',"2023-01-30","18:00"),
('23',"2023-01-31","8:00",'26','32','5','5','600',"2023-02-05","18:00"),
('24',"2023-02-06","8:00",'26','32','5','5','600',"2023-02-11","18:00"),
('25',"2023-02-12","8:00",'26','32','5','5','600',"2023-02-17","18:00"),
('26',"2023-02-18","8:00",'26','32','5','1','600',"2023-02-19","18:00")



SELECT idLocacao , dataLocacao, idCliente,idVendedor,idCarro, marcaCarro, modeloCarro, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega FROM tb_locacao tl 



CREATE TABLE endereco_locacao (
           id_endereco int PRIMARY KEY,
           cidade varchar,
           estado varchar,
           pais varchar 
            )
   
 
   
 INSERT INTO endereco_locacao (id_endereco,cidade,estado,pais)  
 VALUES
 ('1','São Paulo','São Paulo','Brasil'),
 ('2','Rio de Janeiro','Rio de Janeiro','BrasiL'),
 ('3','Belo Horizonte','Minas Gerais','Brasil'),
 ('4','Rio Branco','Acre','Brasil'),
 ('5','Macapá','Amapá','Brasil' ),
 ('6','Porto Alegre','Rio Grande do Sul','Brasil'),
 ('7','Eusébio','Ceará','Brasil'),
 ('8','Campo Grande','Mato Grosso do Sul','Brasil')

 
 INSERT INTO endereco_locacao (id_endereco, cidade,estado,pais)
 VALUES 
 ('9','Manaus','Amazonas','Brasil')

SELECT * FROM endereco_locacao el 


CREATE TABLE endereco_cliente (
           id_cliente int,
           id_endereco int,
           PRIMARY KEY (id_cliente, id_endereco),
           FOREIGN KEY (id_cliente) references tb_cliente(id_cliente),
           FOREIGN KEY (id_endereco) REFERENCES tb_endereco(id_endereco)
)

INSERT INTO endereco_cliente (id_endereco,id_cliente)
VALUES
('1',' 2'),
('2', '3'),
('2', '4'),
('3', '4'),
('3','6'),
('4','10'),
('5','20'),
('6','22'),
('7','23'),
('8','26'),
('9','5')

ALTER TABLE tb_locacao_tempo 
RENAME COLUMN DATA TO datacao
   
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





insert into tb_locacao_tempo 
( datacao, hora, dia, mes,ano, dia_da_semana,dia_da_semana_nome)
values 
("2015-01-10","10:00",'10','1','2015','7', 'Sábado'),
("2015-02-10","12:00",'10','2','2015', '3', 'Terça-feira'),
("2015-02-13","12:00",'13','2','2015','6','Sexta-feira'),
("2015-02-15","12:00",'15','2','2015', '1', 'Domingo'),
("2015-02-15","13:00",'15','2','2015','1', 'Domingo'),
("2015-02-20","13:00",'20','2','2015','6','Sexta-feira'),
("2015-03-02","14:00",'2','3','2015','2','Segunda-feira'),
("2015-03-07","14:00",'7','3','2015','1', 'Domingo'),
("2016-03-02","14:00",'2','3','2016','4','Quarta-feira'),
("2016-03-12","14:00",'12','3','2016','1', 'Domingo'),
("2016-08-02","14:00",'2','8','2016','3', 'Terça-feira'),
("2016-08-12","14:00",'12','8','2016','6','Sexta-feira'),
("2017-01-02","18:00",'2','1','2017','2','Segunda-feira'),
("2017-01-12","18:00",'12','1','2017','5','Quinta-feira'),
("2018-01-02","18:00",'2','1','2018','2','Segunda-feira'),
("2018-01-12","18:00",'12','1','2018','6','Sexta-feira'),
("2018-03-02","18:00",'2','3','2018','6','Sexta-feira'),
("2018-03-12","18:00",'12','3','2018','2','Segunda-feira'),
("2018-04-01","11:00",'1','4','2018','1','Domingo'),
("2018-04-11","11:00",'11','4','2018','4','Quarta-feira'),
("2020-04-01","11:00",'1','4','2020','4','Quarta-feira'),
("2020-04-11","11:00",'11','4','2020','7', 'Sábado'),
("2022-05-01","18:00",'1','5','2022','1', 'Domingo'),
("2022-05-21","18:00",'21','5','2022','7', 'Sábado'),
("2022-06-01","18:00",'1','6','2022','4','Quarta-feira'),
("2022-06-21","18:00",'21','6','2022','3', 'Terça-feira'),
("2022-07-01","18:00",'1','7','2022','6','Sexta-feira'),
("2022-07-21","18:00",'21','7','2022','5','Quinta-feira'),
("2022-08-01","18:00",'1','8','2022','2','Segunda-feira'),
("2022-07-21","18:00",'21','7','2022','5','Quinta-feira'),
("2022-09-01","18:00",'1','9','2022','5','Quinta-feira'),
("2022-09-21","18:00",'21','9','2022','5','Quarta-feira'),
("2022-10-01","18:00",'1','10','2022','1', 'Domingo'),
("2022-10-21","18:00",'21','10','2022','6','Sexta-feira'),
("2022-11-01","18:00",'1','11','2022','3', 'Terça-feira'),
("2022-11-21","18:00",'21','11','2022','2','Segunda-feira'),
("2023-01-02","18:00",'2','1','2023','2','Segunda-feira'),
("2023-01-12","18:00",'12','1','2023','5','Quinta-feira'),
("2023-01-15","18:00",'15','1','2023','1', 'Domingo'),
("2023-01-25","18:00",'25','1','2023','4','Quarta-feira'),
("2023-01-25","18:00",'25','1','2023','4','Quarta-feira'),
("2023-01-30","18:00",'30','1','2023','2','Segunda-feira'),
("2023-01-31","18:00",'31','1','2023','3', 'Terça-feira'),
("2023-02-05","18:00",'5','2','2023','1', 'Domingo'),
("2023-02-06","18:00",'6','2','2023','2','Segunda-feira'),
("2023-02-11","18:00",'11','2','2023','7', 'Sábado'),
("2023-02-12","18:00",'12','2','2023','1', 'Domingo'),
("2023-02-17","18:00",'17','2','2023','6','Sexta-feira'),
("2023-02-18","18:00",'18','2','2023','7', 'Sábado'),
("2023-02-19","18:00",'19','2','2023','1', 'Domingo')

 

CREATE INDEX idx_tb_locacao_tempo_data ON tb_locacao_tempo(datacao)

















