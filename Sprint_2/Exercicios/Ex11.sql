select 
cdcli,
nmcli,
sum(tbsell.qtd * tbsell.vrunt) as gasto
from tbvendas as tbsell
where tbsell.status = 'Concluído'
group by cdcli, nmcli
order by gasto desc 
limit 1