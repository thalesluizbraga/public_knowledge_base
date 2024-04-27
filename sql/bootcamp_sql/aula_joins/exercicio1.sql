-- 1. Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)

select 
	o.order_date,
	o.order_id,
	c.customer_id,
	c.contact_name 
from 
	orders o 
inner join
	customers c on o.customer_id = c.customer_id  

where 
	extract(year from o.order_date) = 1996 





