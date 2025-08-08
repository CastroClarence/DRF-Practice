from backend import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'services', views.ServiceView, basename='service')

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/register/', views.RegisterView.as_view()),
    path('', include(router.urls))
]