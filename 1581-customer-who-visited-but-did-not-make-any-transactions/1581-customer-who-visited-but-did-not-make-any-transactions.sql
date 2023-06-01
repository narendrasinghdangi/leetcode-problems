# Write your MySQL query statement below
select V.customer_id,count(*) as "count_no_trans" from Visits V where V.visit_id not in (select T.visit_id from transactions T) group by V.customer_id;