from django.urls import path
from .views import ListCompany2, JobCreate, job_details, JobUpdate, JobDelete
from .views import ListCompany2, JobCreate, job_details

urlpatterns = [
    path('list/', ListCompany2.as_view(), name='company'),
    path('job_create', JobCreate.as_view(), name='job_create'),
    path('job/<int:pk>/', job_details.as_view(), name='job_details'),
    path('<int:pk>/edit/', JobUpdate.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDelete.as_view(), name='job_delete_urls'),
]
