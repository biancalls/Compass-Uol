#!/Documents/Downloads/Sprint_1/Desafio/ecommerce
mkdir vendas
cp dados_de_vendas.csv vendas
cd ./vendas/
mkdir backup
hoje=$(date + "%Y%M%D")
periodo=$(date + "%Y%M%D %H:%M")
mv dados_de_vendas.csv dados-$hoje.csv
cp dados-$hoje.csv backup
cd ./backup/
mv dados-$hoje.csv backup-dados-$hoje.csv
cd ./vendas/
touch relatorios-$hoje.txt
primeira_vendas=$(head -n 2 backup-dados-$hoje.csv)
ultima_venda=$(tail -n 1 backup-dados-$hoje.csv )
itens_vendidos=$(cut -d ','-f2 backup-dados-$hoje.csv |sort |uniq -c)
dez_primeiras=$(head -f 10 backup-dados-$hoje.csv)
echo "Periodo: $periodo" >> relatorios-$hoje.txt
echo "Primeira venda: $primeira_venda" >> relatorios-$hoje.txt
echo "Ultima venda: $ultima_venda" >> relatorios-$hoje.txt
echo "Itens Vendidos: $itens_vendidos" >> relatorios-$hoje.txt
echo "Dez Primeiras vendas: $dez_primeiras" >> relatorios-$hoje.txt
zip -r backup-dados-$hoje.zip backup-dados-$hoje.csv
rm dados_de_vendas.csv
cd ./backup
rm backup-dados-$hoje.csv
