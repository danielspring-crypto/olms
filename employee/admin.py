from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Department, Employee, Attendance

admin.site.site_header = 'Employee Management System'                  # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'adminsitration'

admin.site.unregister(Group)
admin.site.unregister(User)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['department', 'crew']
	search_fields = ['department',]

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['employee_id', 'employee_name', 'employee_position', 'employee_department', 'employee_salary', 'active_worker', 'date_joined']
	search_fields = ['employee_name',]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance)



# Register your models here.
