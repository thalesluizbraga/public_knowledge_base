-- 5. Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)


select 
	p.product_name,
	p.product_id,
	sum(od.quantity)
	
from 
	products p 
inner join
	order_details od on p.product_id = od.product_id 
group by 
	p.product_name,
	p.product_id 
having 
	sum(od.quantity) < 200
	