-- Write your query below
select c.customer_id, c.customer_name
from customers c
where 1=1
and c.customer_id IN (
    select o.customer_id
    from orders o
    where o.product_name = 'A'
)
and customer_id IN (
    select o.customer_id
    from orders o
    where o.product_name = 'B'
)
and customer_id NOT IN (
    select o.customer_id
    from orders o
    where o.product_name = 'C'
)
order by c.customer_name
