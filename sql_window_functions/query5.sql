-- Query which returns the rank of Iphone 13 in ascending order, partitioned by product_id and based on price

select 
    date,
    product_id,
    model, 
    supplier,
    price,
    row_number() over (partition by product_id order by price asc ) as row_num


from tb_phones
where model = 'iPhone 13'

-- Aqui ele ta ranqueando as linhas, e caso o preço seja igual em duas datas diferentes,
-- ele considera a data mais antiga como rank mais alto