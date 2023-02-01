from django.urls import path

from resumes import views

urlpatterns = [
    path('', views.ResumeListView.as_view(), name='resumes_list'),
    path('<int:pk>/', views.ResumeRetrieveUpdateView.as_view(), name='resume_get_update'),
]
