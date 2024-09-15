select aut.nome
from autor as aut
join livro as liv
   on aut.codautor = liv.autor
join editora as edit
   on edit.codeditora = liv.editora
join endereco as ender
   on ender.codendereco = edit.endereco
where ender.estado <> 'PARANÁ'
   and ender.estado <> 'RIO GRANDE DO SUL'
group by aut.nome  