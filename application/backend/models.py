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
        return f'{self.id} - {self.name}'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        service_id = self.request.query_params.get('service')
        if service_id:
            queryset = queryset.filter(service_id = service_id)
        return queryset
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.service.user

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='service_images/')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.service.user

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='project_images/')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.project.user

class Social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    link = models.URLField()
    platform = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.platform}'    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices={
        'Pending' : 'Pending',
        'Read' : 'Read',
        'Invalid' : 'Invalid'
    })
    image = models.ImageField(upload_to='feedback_images', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'