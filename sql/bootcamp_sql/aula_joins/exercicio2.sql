-- 2. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)

select 
	e.city,
	count(e.employee_id) as employee_count,
	count(c.customer_id) as customer_count
	
from 
	employees e 
left join 
	customers c on e.city  = c.city
group by 
	e.city