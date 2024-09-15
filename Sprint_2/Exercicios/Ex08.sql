select
    sell.cdvdd,
    vdd.nmvdd
from tbvendas as sell
left join tbvendedor as vdd
    on sell.cdvdd = vdd.cdvdd
where sell.status is not null
group by sell.cdvdd
order by count(sell.cdvdd) desc
limit 1