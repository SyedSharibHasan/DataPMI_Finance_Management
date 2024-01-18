from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=150, null=True)
    alt_mobile = models.CharField(max_length=150, null=True)
    position = models.CharField(max_length=150, null=True)
    client_name = models.CharField(max_length=150, null=True)
    client_location = models.CharField(max_length=150, null=True)
    project_director = models.CharField(max_length=150, null=True)
    project_partner = models.CharField(max_length=150, null=True)
    fees = models.CharField(max_length=150, null=True)
    employee_status = models.CharField(max_length=150, null=True)
    joining_date = models.DateField(max_length=150, null=True)
    last_working_date = models.DateField(max_length=150, null=True)
    start_date_of_work_order = models.DateField(max_length=150, null=True)
    end_date_of_work_order = models.DateField(max_length=150, null=True)
    work_order_detail = models.CharField(max_length=150, null=True)
    upload_work_order = models.FileField(upload_to='resume/',max_length=150, null=True)
    upload_nda = models.FileField(upload_to='resume/',max_length=150, null=True)
    upload_resume = models.FileField(upload_to='resume/',max_length=150, null=True)



    
