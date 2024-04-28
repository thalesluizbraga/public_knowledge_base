-- Ordenando os custos de envio pagos por entragador de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;

select 
	o.order_date,
	
	s.shipper_id,
	rank() over (partition by shipper_id order by order_date) as rank_shipper,
	sum(o.freight) as soma_frete,
	lead (sum(o.freight),1) over (order by order_date) as lead_frete,
	lag (sum(o.freight),1) over (order by order_date) as lead_frete
from 
	orders o 
left join
	shippers s on o.ship_via  = s.shipper_id 
group by 
	o.order_date ,
	s.shipper_id 