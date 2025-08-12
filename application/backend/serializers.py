from rest_framework import serializers
from django.contrib.auth.models import User
from backend import models

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            'input_type' : 'password'
        }
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self , data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Password do not match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']

class ServiceImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='service-image-detail'
    )
    class Meta:
        model = models.ServiceImage
        fields = ['url', 'id', 'service', 'image']

class ProjectImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='project-image-detail'
    )

    class Meta:
        model = models.ProjectImage
        fields = ['url', 'id', 'project', 'image']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ['url', 'id', 'name', 'description', 'service']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    images = ServiceImageSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='service-detail'
    )
    class Meta:
        model = models.Service
        fields = ['url', 'id', 'name', 'description', 'projects', 'images']

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'social-detail'
    )
    class Meta:
        model = models.Social
        fields = ['url', 'id', 'platform', 'link']

