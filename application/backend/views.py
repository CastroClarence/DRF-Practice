from django.shortcuts import render
from rest_framework import views, generics, permissions, viewsets
from django.contrib.auth.models import User
from backend import serializers
from backend.permissions import IsOwnerOrReadOnly
from backend.models import Service, Project, ContentImage
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ServiceView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ContentImageView(viewsets.ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = serializers.ContentImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)