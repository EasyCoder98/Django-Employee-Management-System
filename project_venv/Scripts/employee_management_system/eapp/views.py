from django.shortcuts import render,redirect,HttpResponse
from .form import CustomeUserForm,LoginForm,DepartmentForm,EmployeeForm,EmployeeSalaryForm,SalaryReportForm
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        f=CustomeUserForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')
    else:
        f=CustomeUserForm()
        context={'form':f}
        return render(request,'register.html',context)

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(username=uname,password=passw)
        if user is not None:
            request.sessions['uid']=user.id
            login(request,login)
            return redirect('/')
        else:
            return HttpResponse('Invalid creditials')
    else:
        f=LoginForm()
        context={'form':f}
        return render(request,'login.html',context)


 ##Department Views

def d_list(request):
    d=Department.objects.all()
    context={'data':d}
    return render(request,'d_list.html',context)

def add_department(request):
    if request.method=='POST':
        f=DepartmentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/d_list')
    else:
        f=DepartmentForm()
        context={'form':f}
        return render(request,'add_department.html',context)

def edit_department(request,id):
    e=Department.objects.get(id=id)
    if request.method=='POST':
        f=DepartmentForm(request.POST,instance=e)
        if f.is_valid():
            f.save()
            return redirect('/d_list')
    else:
        f=DepartmentForm(instance=e)
        context={'form':f}
        return render(request,'add_department.html',context)
    
def delete_department(request,id):
    e=Department.objects.get(id=id)
    e.delete()
    return redirect('/d_list')  



##Employee Views

def e_list(request):
    d=Employee.objects.all()
    context={'data':d}
    return render(request,'e_list.html',context)

def add_employee(request):
    if request.method=='POST':
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/e_list')
    else:
        f=EmployeeForm()
        context={'form':f}
        return render(request,'add_employee.html',context)

def edit_employee(request,id):
    e=Employee.objects.get(id=id)
    if request.method=='POST':
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save()
            return redirect('/e_list')
    else:
        f=EmployeeForm(instance=e)
        context={'form':f}
        return render(request,'add_employee.html',context)
    
def delete_employee(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/e_list')  



##Salary Views

def s_list(request):
    d=EmployeeSalary.objects.all()
    context={'data':d}
    return render(request,'s_list.html',context)

def add_salary(request):
    if request.method=='POST':
        f=EmployeeSalaryForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/s_list')
    else:
        f=EmployeeSalaryForm()
        context={'form':f}
        return render(request,'add_salary.html',context)

def edit_salary(request,id):
    e=EmployeeSalary.objects.get(id=id)
    if request.method=='POST':
        f=EmployeeSalaryForm(request.POST,instance=e)
        if f.is_valid():
            f.save()
            return redirect('/s_list')
    else:
        f=EmployeeSalaryForm(instance=e)
        context={'form':f}
        return render(request,'add_salary.html',context)
    
def delete_salary(request,id):
    e=EmployeeSalary.objects.get(id=id)
    e.delete()
    return redirect('/s_list')  


##Salary Report Views

def department_salary_costs(request):
    form = SalaryReportForm(request.GET or None)
    salary_data = []

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        salary_data = get_salary_data(start_date, end_date)
    context={'form': form, 'salary_data': salary_data}
    return render(request, 'department_salary_costs.html',context)


def get_salary_data(start_date, end_date):
    data = EmployeeSalary.objects.filter(
        start_date__range=[start_date, end_date]
    ).values('employee__department__name').annotate(total_cost=models.Sum('salary'))

    salary_data = [(entry['employee__department__name'], entry['total_cost']) for entry in data]
    return salary_data


