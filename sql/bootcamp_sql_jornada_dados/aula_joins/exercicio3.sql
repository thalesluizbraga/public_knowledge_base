-- 3. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)



select 
	c.city,
	count(e.employee_id) as employee_count,
	count(c.customer_id) as customer_count
	
from 
	customers c
left join 
	 employees e on c.city = e.city
group by 
	c.city