-- Write your query below
select A.first_name, A.last_name, B.city, B.state
from person A
LEFT JOIN address B
ON A.person_id = B.person_id
