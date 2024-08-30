cd ./home/biancalages/Downloads/Sprint_1/Git_Linux/Desafio/ecommerce/vendas/backup
dia28=$("relatorios-20240828.txt")
dia29=$("relatorios-20240829.txt")
dia30=$("relatorios-20240830.txt")
dia31=$("")
cat "$dia28" "$dia29" "$dia30" "$dia31" > consolidador.txt
awk "{ print $dia28, $dia29, $dia30, $dia31 }" consolidador.txt >> relatorio_final.txt
cp relatorio_final.txt ecommerce