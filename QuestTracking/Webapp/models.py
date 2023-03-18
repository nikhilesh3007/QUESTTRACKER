from django.db import models

# Create your models here.
class CreateTask(models.Model):
    TaskName = models.CharField(max_length=50)
    Description = models.CharField(max_length=800)
    DueDate = models.CharField(max_length=15)
    AssignedEmployee = models.CharField(max_length=30)
    Status = models.CharField(max_length=50)
    StatusDescription = models.CharField(max_length=256)
    Active = models.BooleanField(default=True)
    file = models.FileField(default=False)
class Profiles(models.Model):
    Name = models.CharField(max_length=50)
    EmployeeId = models.CharField(max_length=50)
    EmployeeDesignation = models.CharField(max_length=50)
    Username = models.CharField(max_length=50,default='')
class Projects(models.Model):
    ProjectName = models.CharField(max_length=50)
    ProjectDescription = models.CharField(max_length=800)
    ProjectDeadline = models.CharField(max_length=15)
    AssignedManager = models.CharField(max_length=25)
    Status = models.CharField(max_length=50)
    StatusDescription = models.CharField(max_length=256)
    Active = models.BooleanField(default=True)
    file = models.FileField(default=False)
class File(models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=10)
    EmployeeId = models.CharField(max_length=50)
    Date_Time = models.CharField(max_length=25)
    file = models.FileField(default=False)
class CreateBug(models.Model):
    BugName = models.CharField(max_length=50)
    Description = models.CharField(max_length=800)
    AraiseDate = models.CharField(max_length=25)
    In_Task = models.CharField(max_length=30)
    Status = models.CharField(max_length=20)
    StatusDescription = models.CharField(max_length=256)
    Active = models.BooleanField(default=True)
    file = models.FileField(default=False)


