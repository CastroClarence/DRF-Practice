from backend import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register(r'services', views.ServiceView, basename='service')
router.register(r'projects', views.ProjectView, basename='project')
router.register(r'service-images', views.ServiceImageView, basename='service-image')
router.register(r'project-images', views.ProjectImageView, basename='project-image')
router.register(r'socials', views.SocialView, basename='social')
router.register(r'feedbacks', views.FeedbackView, basename='feedback')

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/register/', views.RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls))
]