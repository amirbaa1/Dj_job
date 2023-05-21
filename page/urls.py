from django.urls import path
from .views import *
from Company.views import JobList

urlpatterns = [
    # path('', HomeView.as_view(), name='home'), # see list company and job in home page home.html.
    path('', ListCompany.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('store/', storeView.as_view(), name='store'),
    path('job/', JobList.as_view(), name='job_list'),
]
