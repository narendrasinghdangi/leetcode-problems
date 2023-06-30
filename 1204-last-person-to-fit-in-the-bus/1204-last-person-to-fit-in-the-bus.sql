# Write your MySQL query statement below
select person_name from (select *, sum(weight) over(order by turn) as total_sum from Queue ) as t where total_sum<=1000 order by turn desc limit 1;