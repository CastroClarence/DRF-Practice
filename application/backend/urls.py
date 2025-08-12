from backend import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'services', views.ServiceView, basename='service')
router.register(r'projects', views.ProjectView, basename='project')
router.register(r'service-images', views.ServiceImageView, basename='service-image')
router.register(r'project-images', views.ProjectImageView, basename='project-image')
router.register(r'socials', views.SocialView, basename='social')

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/register/', views.RegisterView.as_view()),
    path('', include(router.urls))
]