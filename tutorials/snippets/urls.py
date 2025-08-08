from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('snippets/', views.SnippetView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view() ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
