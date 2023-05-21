from django.urls import path
from .views import ListCompany2, JobCreate,job_detile

urlpatterns = [
    path('list/', ListCompany2.as_view(), name='company'),
    path('job_create', JobCreate.as_view(), name='job_create'),
    path('job/<int:pk>/', job_detile.as_view(), name='job_detile'),
]
