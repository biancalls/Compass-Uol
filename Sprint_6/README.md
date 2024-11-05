# **Sprint 6- Dockerfile e Sistema AWS** 

## **O que foi feito nessa Sprint 6?**

Nessa Sprint 6 tivemos mais cursos dos serviços disponibilizados dentro da AWS, com laboratório dos serviços Athena e Lambda.

## **01-Laboratório Athena**

O Laboratorío Athena propostos nessa sprint consistiam na prática de queries usando como banco de dados o arquivo csv chamado "nomes.csv", a criação do bucket referente foi feito na sprint passada e estou aproveitando o mesmo bucket.

**01. PASTA QUERIES**

![QUERIES](../Sprint_6/Evidências/Exercício/Athena/pastaquerie.png)

**CRIAÇÃO DE TABELA**

![CREATE](../Sprint_6/Evidências/Exercício/Athena/createtable-athena.png)

**QUERIE DE TESTE**

![QUERIE2](../Sprint_6/Evidências/Exercício/Athena/querie2-athena.png)

**RESULTADO QUERIE**

![RESULTADO1](../Sprint_6/Evidências/Exercício/Athena/resultado-teste-athena.png)

**QUERIE PEDIDA**

![QUERIE3](../Sprint_6/Evidências/Exercício/Athena/querie3-athena.png)

**RESULTADO QUERIE**

![RESULTADO2](../Sprint_6/Evidências/Exercício/Athena/RESULTADO-LAB.png)

## **02-Laboratório LAMBDA**

**CRIAÇÃO DE FUNÇÃO**

![FUNCTION](../Sprint_6/Evidências/Exercício/Lambda/function-lambda.png)

**CONSTRUÇÃO CÓDIGO**

![PYTHON](../Sprint_6/Evidências/Exercício/Lambda/test-lambda.png)

**CRIAÇÃO LAYER**

![LAYER](../Sprint_6/Evidências/Exercício/Lambda/panda-layer-lambda.png)

**DOCKERFILE**

````dockerfile

FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
python3-pip \
zip
RUN yum -y clean all

````

**BUILD CONTAINER LAMBDA**

![BUILD-LAMBDA](../Sprint_6/Evidências/Exercício/Lambda/build-lambda.png)

**RUN BASH LAMBDA CONTAINER**

![BASH-LAMBDA](../Sprint_6/Evidências/Exercício/Lambda/run-lambda.png)

**CONTAINER LAMBDA**

![CONTAINER](../Sprint_6/Evidências/Exercício/Lambda/containr-lambda.png)

**PIP INSTALL PANDAS**

![INSTALL](../Sprint_6/Evidências/Exercício/Lambda/sucess-install-lambda.png)

**ARQUIVO PARA ZIP E COPIA**

![COPIA](../Sprint_6/Evidências/Exercício/Lambda/copie-lambda.png)

**UPLOAD NO BUCKET S3 ARQUIVO ZIP**

![UPLOAD](../Sprint_6/Evidências/Exercício/Lambda/upload-zip-lambda.png)

**ADICIONAR CAMADA PANDALAYER NO LAMBDA**

![CHANGE](../Sprint_6/Evidências/Exercício/Lambda/change-function.png)

**TESTE LAMBDA**

![TESTE](../Sprint_6/Evidências/Exercício/Lambda/test-lambda.png)

**RESULTADO SCRIPT PYTHON LAMBDA**

![RESULTADO](../Sprint_6/Evidências/Exercício/Lambda/resultado-lambda.png)

## **Certificados AWS**

![BEST-PRATICE](../Sprint_6/Evidências/Certificados/bestpratice.png)

![ATHENA](../Sprint_6/Evidências/Certificados/athena.png)

![EMR](../Sprint_6/Evidências/Certificados/emr.png)

![GLUE](../Sprint_6/Evidências/Certificados/glue.png)

![ANALYTICS-PART1](../Sprint_6/Evidências/Certificados/analytics-part1.png)

![ANALYTICS-PART2](../Sprint_6/Evidências/Certificados/analytics-parte2.png)

![QUICKSITE](../Sprint_6/Evidências/Certificados/quicksite.png)

![REDSHIFT](../Sprint_6/Evidências/Certificados/redshift.png)

![SERVERLESS](../Sprint_6/Evidências/Certificados/serverless.png)

## **Dificuldades**

Nessa Sprint a maior dificuldade que tive foi a conecção que tive que fazer com o sistema AWS, devido ao problema com as permissões do provedor de internet que dificultaram a execução do laboratório e desafio,foi feito pelo terminal do Pycharm usando um comando no terminal , até o mesmo o desafio, tive que colocar as acess key no documento porque pelo terminal o envio não estava dando o resultado querido. Contudo , tive ajuda do meus colegas de SQUAD e turma que ajudaram na execução das atividades. 
