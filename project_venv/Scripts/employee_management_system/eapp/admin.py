from django.contrib import admin
from .models import Department,Employee,EmployeeSalary
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name','floor']
    search_fields=['name']

admin.site.register(Department,DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email', 'designation', 'reporting_manager', 'department']
    list_filter=['designation','department']
    search_fields=['name','email']

admin.site.register(Employee,EmployeeAdmin)


class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display=['employee','salary','start_date','end_date']
    list_filter=['start_date','end_date']
    search_fields=['employee__name']

admin.site.register(EmployeeSalary,EmployeeSalaryAdmin)