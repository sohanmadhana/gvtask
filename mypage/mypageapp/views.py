
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect

from django.urls import reverse

from .models import Employee
from .forms import EmpForm
# Create your views here.

def employee(request):
    
    if 'status' in request.POST:
        if 'Active Employees' == request.POST.get('status'):
            employee = Employee.objects.filter(status=True)
            return render(request, 'employee_details.html',{ 'employee':employee })
        elif 'Inactive Employees' == request.POST.get('status'):
            employee = Employee.objects.filter(status=False)
            return render(request, 'employee_details.html',{ 'employee':employee })
        elif 'All Employees' == request.POST.get('status') :
            employee = Employee.objects.all()
            return render(request, 'employee_details.html',{ 'employee':employee })
        
    employee = Employee.objects.all()
    return render(request, 'employee_details.html',{ 'employee':employee })

def addEmployee(request):
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
    context = {'form' : form}
    return render(request, "emp_form.html", context)

def editEmployee(request,id):
    print(str(id))
    emp = Employee.objects.get(id=id)
    print(str(emp.status))
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST, instance=emp)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.author = request.user
            emp.save()
            return redirect('employee')
    else:
        form = EmpForm(instance=emp)
    context = {'form': form}
    return render(request, "emp_form.html", context)

def deleteEmployee(request,id):
    if request.user.is_superuser:
        emp = Employee.objects.get(id=id)
        emp.delete()
        return redirect('employee')

def updateStatus(request,id):
    emp = Employee.objects.get(id=id)
    if emp.status == True:
        emp.status = False
        emp.save()
        return redirect('employee')
    elif emp.status == False:
        emp.status = True
        emp.save()
        return redirect('employee')
    
  
