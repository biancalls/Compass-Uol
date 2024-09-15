select 
   cdven
from tbvendas
where status = 'Em aberto'
     and deletado <> 0
order by cdven asc
