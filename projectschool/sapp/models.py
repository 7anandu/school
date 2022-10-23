from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




class Person(models.Model):
    name = models.CharField(max_length=124)
    DOB = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Phnum = models.IntegerField()
    Address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name