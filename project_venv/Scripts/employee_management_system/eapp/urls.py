"""
URL configuration for employee_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('register',v.register,name='register'),
    path('login',v.login_view,name='login'),

    path('d_list',v.d_list,name='d_list'),
    path('add_department',v.add_department,name='add_department'),
    path('edit_d/<int:id>/',v.edit_department,name='edit_d'),
    path('delete_d/<int:id>',v.delete_department,name='delete_d'),

    path('e_list',v.e_list,name='e_list'),
    path('add_employee',v.add_employee,name='add_employee'),
    path('edit_e/<int:id>/',v.edit_employee,name='edit_e'),
    path('delete_e/<int:id>',v.delete_employee,name='delete_e'),

    path('s_list',v.s_list,name='s_list'),
    path('add_salary',v.add_salary,name='add_salary'),
    path('edit_s/<int:id>',v.edit_salary,name='edit_s'),
    path('delete_s/<int:id>',v.delete_salary,name='delete_s'),

    path('department_salary_costs',v.department_salary_costs, name='department_salary_costs'),
]
