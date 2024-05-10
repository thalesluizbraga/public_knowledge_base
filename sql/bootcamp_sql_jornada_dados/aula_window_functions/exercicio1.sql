-- Faça a classificação dos produtos mais vendidos usando usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
-- Tabelas utilizadasFROM order_details o JOIN products p ON p.product_id = o.product_id;




select 
	p.product_id,
	sum(od.quantity) as quantidade,
	rank() over (order by sum(od.quantity) desc) rank_produto,
	dense_rank() over (order by sum(od.quantity) desc) dens_rank_produto,
	row_number () over (order by sum(od.quantity) desc) row_number_produto
	
from 
	products p 
left join
	order_details od on p.product_id = od.product_id 
group by 
	p.product_id 