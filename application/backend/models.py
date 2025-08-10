from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    user = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Project(models.Model):
    service = models.ForeignKey(Service, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        service_id = self.request.query_params.get('service')
        if service_id:
            queryset = queryset.filter(service_id = service_id)
        return queryset
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.service.user

class ContentImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE, blank=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='content_images/')