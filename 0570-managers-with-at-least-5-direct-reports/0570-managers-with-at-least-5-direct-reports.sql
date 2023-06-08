# Write your MySQL query statement below
select E1.name from Employee E1 inner join Employee E2 on E1.id=E2.managerId group by E1.name having count(E1.name)>=5;