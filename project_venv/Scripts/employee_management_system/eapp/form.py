from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Department,Employee,EmployeeSalary
 
class CustomeUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model=EmployeeSalary
        fields='__all__'


class SalaryReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))