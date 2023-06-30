# Write your MySQL query statement below
select product_id, 10 as price from Products group by product_id having min(change_date) > "2019-08-16" 
union
select p.product_id , P.new_price as price from products P where (p.product_id,p.change_date) in (
select product_id, max(change_date) as recent_date
from Products
where change_date <= "2019-08-16"
group by product_id
);