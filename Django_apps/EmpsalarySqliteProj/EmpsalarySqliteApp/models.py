from django.db import models

class Employee(models.Model):
    empno = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=200)
    basic_salary = models.FloatField()

    def __str__(self):
        return f"Employee number: {self.empno}, Employee Name: {self.emp_name}"
