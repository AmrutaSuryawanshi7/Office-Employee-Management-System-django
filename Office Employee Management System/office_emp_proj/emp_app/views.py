from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all_emp(request):
    all_emp = Employee.objects.all()
    context = {
        "all_emp" : all_emp
        }
    print(context)
    return render(request, 'view_all_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        
        first_name = request.POST['first_n']
        last_name = request.POST['last_n']
        dept = int(request.POST['dept_name'])
        salary = int(request.POST['sal'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone_no'])
        # hire_date = request.POST['hire_date']
        
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        
        return HttpResponse("Employee added successfully!!")
        
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return HttpResponse("Exception occured. Unable to add employee.")

def remove_emp(request, emp_id=0):
    
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employee removed successfully!!")
            
        except:
            return HttpResponse("Unable to remove selected employee")
    all_emps1 = Employee.objects.all()
    context1 = {
        "all_emps_to_remove" : all_emps1
    }
    return render(request, 'remove_emp.html',context1)

def filter_emp(request):
    
    if request.method == 'POST':
        name = request.POST['first_n']
        dept = request.POST['dept_name']
        role = request.POST['role']

        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
    
        context2 = {
            "all_emp" : emps
        }
        return render(request, "view_all_emp.html",context2)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse('Unable to filter.')