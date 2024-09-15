select 
  tbsell.cdpro,
  tbsell.nmcanalvendas,
  tbsell.nmpro,
  sum(tbsell.qtd) as quantidade_vendas
from tbvendas as tbsell
left join tbestoqueproduto as tbpro
       on tbsell.status = tbpro.status
where tbsell.status = 'Concluído'
group by tbsell.cdpro, tbsell.nmcanalvendas
order by quantidade_vendas  
limit 10