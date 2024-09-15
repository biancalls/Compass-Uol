select 
aut.nome as nome
from autor as aut
left join livro as liv 
     on aut.codautor = liv.autor
where titulo is null
group by nome
order by nome 
     