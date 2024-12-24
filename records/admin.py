from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RegisterEmployee)
admin.site.register(models.Enterprise)
admin.site.register(models.Sector)
admin.site.register(models.RegisterKey)
admin.site.register(models.RegisterEPI)
