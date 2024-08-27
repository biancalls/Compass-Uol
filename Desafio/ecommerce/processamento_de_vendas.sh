cd /home/biancalages/Downloads/Sprint_1/Sprint_1/Desafio/ecommerce
mkdir vendas
cp dados_de_vendas.csv vendas
cd vendas
mkdir backup
hoje=$(date +"%Y%m%d")
periodo=$(date +"%Y%m%d %H:%M")
cp dados_de_vendas.csv dados-$hoje.csv
cp dados-$hoje.csv backup/backup-dados-$hoje.csv
cd backup
touch relatorios-$hoje.txt
primeira_vendas=$(head -n 2 backup-dados-$hoje.csv | cut -d ',' -f 5)
ultima_venda=$(tail -n 1 backup-dados-$hoje.csv | cut -d ',' -f 5)
itens_vendidos=$(tail -n +2 backup-dados-$hoje.csv |cut -d ',' -f 2 |sort |uniq | wc -l)
dez_primeiras=$(head backup-dados-$hoje.csv)
echo "Periodo: $periodo" >> relatorios-$hoje.txt
echo "Primeira venda: $primeira_vendas" >> relatorios-$hoje.txt
echo "Ultima venda: $ultima_venda" >> relatorios-$hoje.txt
echo "Itens Vendidos: $itens_vendidos" >> relatorios-$hoje.txt
echo "Dez Primeiras vendas: $dez_primeiras" >> relatorios-$hoje.txt
zip -r backup-dados-$hoje.zip backup-dados-$hoje.csv
rm backup-dados-$hoje.csv
cd ../
rm dados_de_vendas.csv


