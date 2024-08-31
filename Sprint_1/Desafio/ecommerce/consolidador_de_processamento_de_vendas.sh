cd /home/biancalages/Downloads/Sprint_1/Git_Linux/Desafio/ecommerce/vendas/backup
dia28=$(cat relatorios-20240828.txt)
dia29=$(cat relatorios-20240829.txt)
dia30=$(cat relatorios-20240830.txt)
dia31=$(cat relatorios-20240831.txt)
touch relatorio_final.txt
echo "$dia28" >> relatorio_final.txt
echo "$dia29" >> relatorio_final.txt
echo "$dia30" >> relatorio_final.txt
echo "$dia31" >> relatorio_final.txt
