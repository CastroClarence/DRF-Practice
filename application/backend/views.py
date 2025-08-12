from django.shortcuts import render
from rest_framework import views, generics, permissions, viewsets
from django.contrib.auth.models import User
from backend import serializers
from backend.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from backend.models import Service, Project, ServiceImage, ProjectImage, Social, Feedback
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class RegisterView(generics.CreateAPIView):
    """
    A view that enables Create function for User
    """
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer

class UserView(generics.ListAPIView):
    """
    A view that enables List function for User
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    """
    A view that enables Retrieve function for User
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ServiceView(viewsets.ModelViewSet):
    """
    A view that enables CRUD function for Services
    """
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ProjectView(viewsets.ModelViewSet):
    """
    A view that enables CRUD function for Projects
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class ServiceImageView(viewsets.ModelViewSet):
    """
    A view that enables CRUD function for Service Images
    """
    queryset = ServiceImage.objects.all()
    serializer_class = serializers.ServiceImageSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)

class ProjectImageView(viewsets.ModelViewSet):
    """
    A view that enables CRUD function for Project Images
    """
    queryset = ProjectImage.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ProjectImageSerializer

class SocialView(viewsets.ModelViewSet):
    """
    A view that enables CRUD function for Socials
    """
    queryset = Social.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SocialSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FeedbackSerializer