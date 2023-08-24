Select * From EmployeeApp_departments

Select * From EmployeeApp_departments

Insert into EmployeeApp_departments (DepartmentName) Values('HR');
Insert into EmployeeApp_departments (DepartmentName) Values('Accounting');
Insert into EmployeeApp_departments (DepartmentName) Values('Financing');
Insert into EmployeeApp_departments (DepartmentName) Values('Compliance');


Select * From EmployeeApp_employees;

Insert into EmployeeApp_employees (EmployeeName, Department, DateOfJoining, PhotoFileName) 
            Values('Mahmoud', '1', Date("2023-03-01T08:00:00Z"), 'urls');

Insert into EmployeeApp_employees (EmployeeName, Department, DateOfJoining, PhotoFileName) 
            Values('Menah', '2', Date("2023-12-01T08:00:00Z"), 'urls urls');
            
Insert into EmployeeApp_employees (EmployeeName, Department, DateOfJoining, PhotoFileName) 
            Values('Fatmah', '2', Date("2023-08-19T08:00:00Z"), 'urls urls urls');

Insert into EmployeeApp_employees (EmployeeName, Department, DateOfJoining, PhotoFileName) 
            Values('Hossam', '2', Date("2023-12-15T08:00:00Z"), 'urls urls urls urls');


