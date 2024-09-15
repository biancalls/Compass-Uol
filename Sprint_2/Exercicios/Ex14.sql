select 
 estado,
 round(avg(tbsell.qtd * tbsell.vrunt),2) as gastomedio
from tbvendas as tbsell
where status = 'Concluído'
group by estado 
order by gastomedio desc