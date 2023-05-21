from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Company, Job


class ListCompany2(ListView):
    model = Company
    template_name = 'company.html'
    context_object_name = 'comp_view'


class JobCreate(CreateView):
    model = Job
    template_name = 'job_create.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'text']


class JobList(ListView):
    model = Job
    template_name = 'job.html'
    context_object_name = 'job_list'


class job_details(DeleteView):
    model = Job
    template_name = 'job_detile.html'
    context_object_name = 'job_details'
