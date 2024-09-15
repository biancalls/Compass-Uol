select count (*) as quantidade, nome, estado, cidade
from livro as liv
join endereco as ender on ender.CodEndereco = edit.endereco
join editora as edit on edit.codEditora = liv.editora
group by editora
order by quantidade desc