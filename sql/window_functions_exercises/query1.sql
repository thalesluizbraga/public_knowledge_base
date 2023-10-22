-- Query which returns the min, max and average price by product and model

select 
    product_id,
    model,
    min(price) as min_price,
    max(price) as max_price,
    round(avg(price),2) as avg_price

from tb_phones
group by product_id, model