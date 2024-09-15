select 
   aut.codautor,
   aut.nome,
   count(distinct liv.titulo) as quantidade_publicacoes
from autor as aut   
left join livro as liv  
       on aut.codautor = liv.autor
group by aut.codautor, nome 
order by quantidade_publicacoes desc
limit 1