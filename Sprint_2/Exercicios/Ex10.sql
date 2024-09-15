select 
tbvdd.nmvdd as vendedor,
sum(tbsell.qtd * tbsell.vrunt) as valor_total_vendas,
round(sum(tbsell.qtd * tbsell.vrunt) * tbvdd.perccomissao/100,2) as comissao
from tbvendas as tbsell 
join tbvendedor as tbvdd
      on tbvdd.cdvdd = tbsell.cdvdd
where tbsell.status = 'Concluído'
group by tbvdd.nmvdd
order by round(sum(tbsell.qtd * tbsell.vrunt) * tbvdd.perccomissao/100,2) desc 