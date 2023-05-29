from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Company, Job
from django.urls import reverse_lazy


class ListCompany2(ListView):
    model = Company
    template_name = 'company.html'
    context_object_name = 'comp_view'
    ordering = ['-id']


class JobCreate(CreateView):
    model = Job
    template_name = 'job_create.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'text']


class JobList(ListView):
    model = Job
    template_name = 'job.html'
    context_object_name = 'job_list'
    ordering = ['-id']


class job_details(DeleteView):
    model = Job
    template_name = 'job_detile.html'
    context_object_name = 'job_details'


class JobUpdate(UpdateView):
    model = Job
    template_name = 'job_update.html'
    fields = '__all__'
    context_object_name = 'up_job'


class JobDelete(DeleteView):
    model = Job
    template_name = 'job_delete.html'
    success_url = reverse_lazy('job_list')
    context_object_name = 'job_delete'
