from backend import views
from django.urls import path, include
urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/register/', views.RegisterView.as_view())
]