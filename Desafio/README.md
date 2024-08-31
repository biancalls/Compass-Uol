# **Sprint 1 - Git e Linux**

## **Sobre o Desafio:**

O desafio pedia a geração de processos e relários de vendas de um ecommerce com base nos arquivos csv vindos deste ecommerce. 

## **Etapas**

**1. Criação do arquivo.sh executável e diretórios** 

Foi pedido a criação de um arquivo executável de nome processamento_de_vendas.sh (cd /home/biancalages/Downloads/Sprint_1/Git_Linux/Desafio/ecommerce) , dentro dele deve conter um script contendo os comandos para criação de um diretório vendas (mkdir vendas) e uma copia do arquivo dados_de_vendas.csv (cp dados_de_vendas.csv vendas). Foi feito o comando para a criação da variável $hoje(hoje=$(date + %Y%m%d)) e a variável $periodo(periodo=$(date + %Y%m%d %H : %M)) onde identificava a data e as horas no relatórios.txt gerados nas execuções do arquivo.sh durante 4 dias consecutivos diferenciandos pela data do processamento . Dentro desse diretório vendas o arquivo csv foi renomeado dados-20240824.csv( cp dados_de_vendas.csv dados-$hoje.csv), uma copia renomeada do arquivo csv e a criação de outro diretório chamado backup ( cp dados-$hoje.csv backup/backup-dados-$hoje.csv).  



 ![Screenshotinicial](https://github.com/biancalls/Sprint_1/blob/main/Evidencias/Screenshot%20from%202024-08-30%2015-46-47.png)




**2. Captação do conteúdo do relatório.txt gerado** 

O processamento desse arquivo.sh, usando os dados da copia backup-dados-$hoje.csv, gera um relatorios-$hoje.txt (touch relatorios-$hoje.txt), neste deve conter ,na primeira linha, a data e a hora do processamento do arquivo ( echo "Periodo: $periodo" >> relatorios-$hoje.txt) , em seguida a captanção da data do primeiro registro de venda no arquivo.csv ( primeira_vendas=$(head -n 2 backup-dados-$hoje.csv | cut -d ',' -f 5) e envia a informação ao arquivo relatorios-$hoje.txt ( echo "Primeria venda: $primeira_venda" >> relatorios-$hoje.txt). Logo depois a captação do ultimo registro de venda contido no arquivo ( ultima_venda=$(tail -n 1 backup-dados-$hoje.csv | cut -d ',' -f 5) que é enviado para o arquivo relatorios-$hoje.txt ( echo "Ultima venda: $ultima_venda" >> relatorios-$hoje.txt). A quantidade total de itens diferentes foi pedida ( itens_vendidos=$(tail -n +2 backup-dados-$hoje.csv | cut -d ',' -f 2 | sort |uniq | wc -l) e também enviada para o arquivo relatorios-$hoje.txt ( echo "Itens Vendidos: $itens_vendidos >> relatorios-$hoje.txt) . Foi requisitado que o arquivo relatorios-$hoje.txt tenha as 10 primeiras linhas do arquivo backup-dados-$hoje.csv (dez_primeiras=$(head backup-dados-$hoje.csv)) e enviado para finalizar o relatorios-$hoje.txt ( echo "Dez primeiras linhas: $dez_primeiras" >> relatorios-$hoje.txt).


![linhas](https://github.com/biancalls/Sprint_1/blob/main/Evidencias/Screenshot%20from%202024-08-30%2015-47-11.png) 



**3. Redução do espaço em disco**

A compactação dos arquivo backup-dados-$hoje.csv devido ao tamanho do diretório ecommerce ( zip -r backup-dados-$hoje.zip backup-dados-$hoje.csv).Foi removido o arquivo backup-dados-$hoje.txt e dados_de_vendas.csv do diretório vendas ( rm backup-dados-$hoje.csv cd../  rm dados_de_vendas.csv)


![linhasfinais](https://github.com/biancalls/Sprint_1/blob/main/Evidencias/Screenshot%20from%202024-08-30%2015-47-40.png)


**4. Comando crontab**

Foi feito um agendamento de executação do script contido no arquivo.sh processamento_de_vendas.sh, durante quatro dias consecutivos, de quarta-feira a sábado as 15:27 

![crontab](https://github.com/biancalls/Sprint_1/blob/main/Evidencias/Screenshot%20from%202024-08-28%2010-43-35.png) 

**5. Criando um novo relátorio**

Ao final dos processamentos diarios, foi pedido um  script em um novo arquivo.sh executável consolidador_de_processamento_de_vendas.sh que consolidasse todos os arquivos.txt gerados em unico outro arquivo relatorio_final.txt 


![Secreenshots do codigo consolidador


![Scrennshots do tree 

## **Dificuldades**

Durante a execução desse desafio enfretei algumas dificuldades tecnicas, devido a falta de experiência na área e com os programas em questão (Git e Linux). Erros de grafia de comamdos, fiz comandos errados que me resultou na perda de arquivos e diretórios, tive problemas configuração inicial do git hub e do linux , que me tiram dias de rendimento porém adquiri conhecimentos durante a resolução desse problemas, além do material didatico disponibilizado para mim, a minha turma do estágio e meu SQUAD ajudaram significativamente, assim como os foruns dessas plataformas, pequisas onlines e videos no youtube me ajudaram a compreender o linguajar e tecnico dessas plataformas para a conclusão desse desafio. 




