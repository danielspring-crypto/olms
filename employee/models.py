from django.db import models

# Create your models here.
class Department(models.Model):
	department = models.CharField(max_length=255)
	crew = models.IntegerField()

	def __str__(self):
		return self.department

class Employee(models.Model):
	employee_id = models.CharField(max_length=255)
	employee_name = models.CharField(max_length=255)
	employee_position = models.CharField(max_length=255)
	employee_department = models.ForeignKey(Department, on_delete=models.CASCADE)
	employee_salary = models.CharField(max_length=255)
	active_worker = models.BooleanField(default=True)
	date_joined = models.DateField()
	feedback = models.TextField()

	def __str__(self):
		return self.employee_name

class Attendance(models.Model):
	date = models.DateField()
	time = models.TimeField()
	employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
	note = models.TextField()

