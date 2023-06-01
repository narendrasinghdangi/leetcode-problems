# Write your MySQL query statement below
select P.product_name,S.year,S.price from sales S left join product P on P.product_id=S.product_id;