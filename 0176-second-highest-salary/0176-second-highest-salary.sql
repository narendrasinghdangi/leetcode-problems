# Write your MySQL query statement below

select max(E1.salary) as SecondHighestSalary from Employee E1 where E1.salary<>(select max(E2.salary) from Employee E2)