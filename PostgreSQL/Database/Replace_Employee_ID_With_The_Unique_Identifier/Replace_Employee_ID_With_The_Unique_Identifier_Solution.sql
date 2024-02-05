SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
RIGHT JOIN Employees ON EmployeeUNI.id = Employees.id
ORDER BY 1 ASC;
