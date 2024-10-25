from django.db import models

# Create your models here.
class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
            return self.name
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default= 'Sin apellido')
    email = models.EmailField()
    document = models.CharField(max_length=20, unique=True)
    phone_number =  models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    date_of_birth =  models.DateField(null=True)
    years_of_experience = models.IntegerField(null=True)
    gender =  models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.first_name