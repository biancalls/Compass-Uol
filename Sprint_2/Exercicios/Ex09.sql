select 
prod.cdpro,
tbsell.nmpro 
from tbestoqueproduto as prod
left join tbvendas as tbsell    
      on prod.cdpro = tbsell.cdpro
where (tbsell.dtven) between '2014-02-03' and '2018-02-02'
group by prod.cdpro
order by count (tbsell.cdpro) desc 
limit 1