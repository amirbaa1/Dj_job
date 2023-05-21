from django.urls import path
from .views import *
from Company.views import JobList, JobCreate

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', ListCompany.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    #path('job/', jobView.as_view(), name='job'),
    path('store/', storeView.as_view(), name='store'),
    path('job/', JobList.as_view(), name='job_list'),
]
