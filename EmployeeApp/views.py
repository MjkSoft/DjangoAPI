from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.core.files.storage import default_storage


@csrf_exempt        # home page added code although it doen't work
def home(request):
    return render(request, 'home.html',{})

@csrf_exempt        # About page 
def about(request):
    return render(request, 'about.html',{})


# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Faild to Add", safe=False)
    
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Faild to Update", safe=False)
    
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Faild to Add", safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Faild to Update", safe=False)
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)    


@csrf_exempt
def SaveFile(request):
    if request.method == 'POST' and request.FILES.get('uploadedFile'):
        file = request.FILES['uploadedFile']
        file_name = default_storage.save(file.name, file)
        return JsonResponse(file_name, safe = False)
    else:
        return JsonResponse({'message': 'No File uploaded'})
        
