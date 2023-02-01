from django.urls import include, path

urlpatterns = [
    path('resume/', include('resumes.urls')),
    path('auth/', include('rest_framework.urls')),
]
