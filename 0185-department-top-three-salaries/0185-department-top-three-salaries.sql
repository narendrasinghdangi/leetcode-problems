# Write your MySQL query statement below
select D.name as Department , E.name as Employee , E.salary from Department D join Employee E on D.id=E.departmentID 
where  3 > (select count(distinct (e2.Salary))
        from  Employee e2
        where e2.Salary > E.Salary
            and E.DepartmentId = e2.DepartmentId)