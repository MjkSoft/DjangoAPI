from django.contrib import admin
# from EmployeeApp.views import home, about

# Register your models here.
from .models import Employees, Departments

admin.site.register(Employees)
admin.site.register(Departments)
# .site.register(home)
# admin.site.register(about)