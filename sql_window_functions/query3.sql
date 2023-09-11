-- Query which returns the price difference by day, product id, model and supplier in dates between 20203-01-01 and 2023-01-31

select
    date,
    product_id,
    model,
    supplier,
    lag(price,1) over (partition by product_id, supplier order by date ) as previous_price,
    price - (lag(price,1) over (partition by product_id, supplier order by date)) as price_difference,
    ROUND(
         ((price - LAG(price) OVER(PARTITION BY product_id, supplier ORDER BY date)) 
          / LAG(price) OVER(PARTITION BY product_id, supplier ORDER BY date)) 
         * 100, 2) AS price_difference_percentage


from tb_phones
  

-- The lag function takes a given number of rows before the current row. The partition by clause is responsable
-- for ordering the rows by parameters

