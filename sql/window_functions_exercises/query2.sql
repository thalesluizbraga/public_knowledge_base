-- Query which returns the difference of price between SupplierA and SupplierB products in 2023-01-01

with tb_supplierA as(

    select 
        model,
        price

    from tb_phones
    where supplier='SupplierA' and date='2023-01-01' 

),

tb_supplierB as(

    select 
        model,
        price
    
    from tb_phones
    where supplier='SupplierB' and date='2023-01-01'

)

select 
    ta.model,
    ta.price,
    tb.price,
    (ta.price - tb.price) as price_diff

from tb_supplierA as ta
left join tb_supplierB as tb on ta.model = tb.model

