-- 6. Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)


select 
	c.customer_id,
	count(o.order_id) as total_pedidos
	
from
	orders o 
left join
	customers c on o.customer_id = c.customer_id 
where 
	o.order_date >= '1996-12-31'
group by 
	c.customer_id 
having 
	count(o.order_id) > 15

	