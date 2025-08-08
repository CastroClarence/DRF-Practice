from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    user = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
