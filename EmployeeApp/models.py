from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    def __str__(self):
        return self.DepartmentName


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.EmployeeName}  - {self.DateOfJoining}"
    
    