from django.db import models

# Create your models here.
class Student(models.Model):
    surname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    othername = models.CharField(max_length = 50)
    dob = models.DateField()
    address = models.TextField()
    phone_number = models.IntegerField()
    gender = [('M', 'Male'),('F', 'Female')]
    cgpa = models.IntegerField()

    def __str__(self):
        return self.surname + ' ' + self.firstname
    
class Guardian(models.Model):
    surname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    othername = models.CharField(max_length = 50)
    occupation = models.CharField(max_length = 50)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.surname + ' ' + self.firstname
