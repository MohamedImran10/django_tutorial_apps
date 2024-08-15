from django.shortcuts import render, redirect,get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def home(request):
    return render(request, 'home.html')

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def delete_employee(request, empno):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, empno=empno)
        employee.delete()
    return render(request, 'delete_employee.html', {'empno': empno})
    
def salary_report(request):
    employees = Employee.objects.all()
    report = []
    for emp in employees:
        basic = emp.basic_salary
        da = basic * 0.80
        hra = basic * 0.15
        ma = basic * 0.10
        gross = basic + da + hra + ma
        report.append({
            'empno': emp.empno,
            'emp_name': emp.emp_name,
            'basic_salary': basic,
            'da': da,
            'hra': hra,
            'ma': ma,
            'gross_salary': gross
        })
    for r in report:
        print(r)
    return render(request, 'salary_report.html', {'report': report})


