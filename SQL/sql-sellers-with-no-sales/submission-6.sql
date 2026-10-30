-- Write your query below
select S.seller_name
from seller S
where S.seller_id not IN (
    select seller_id
    from orders O
    where sale_date >= '2020-01-01' and sale_date < '2021-01-01'
)
order by seller_name
