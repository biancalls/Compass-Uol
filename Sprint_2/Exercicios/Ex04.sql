select 
aut.nome as nome, 
aut.codautor as codautor,
aut.nascimento as nascimento,
count (distinct titulo) as quantidade
from autor as aut
left join livro as liv
    on aut.codautor = liv.autor
group by nome 
order by nome , quantidade