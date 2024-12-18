from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    
class Enterprise(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class RegisterEmployee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    credential = models.PositiveIntegerField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    
