-- Query which returns the rank of Iphone 13 in ascending order, partitioned by product_id and based on price

select 
    date,
    product_id,
    model,
    supplier, 
    price,
    rank() over (partition by product_id order by price asc ) as price_rank

from tb_phones
where model = 'iPhone 13'

-- Aqui ele ta ranqueando os preços, e se houver um caso de 2 preços iguais ele atribui a mesma posiçao.date

