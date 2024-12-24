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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    
class RegisterKey(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Chave: {self.name} | Número: {self.number}'
    
    
class RegisterEPI(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(default=1)
    description = models.TextField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
    
