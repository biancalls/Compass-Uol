select 
depp.cddep,
depp.nmdep,
depp.dtnasc,
sum(tbsell.qtd * tbsell.vrunt) as valor_total_vendas
from tbdependente as depp 
left join tbvendas as tbsell
   on depp.cdvdd = tbsell.cdvdd
where tbsell.status = 'Concluído'
group by depp.cddep, depp.nmdep
order by valor_total_vendas
limit 1