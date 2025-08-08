from django.shortcuts import render
from rest_framework import views, generics, permissions, viewsets
from django.contrib.auth.models import User
from backend import serializers
from backend.permissions import IsOwnerOrReadOnly
from backend.models import Service
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