from django.db import models
from django.urls import reverse


class Company(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    name_partners = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Job(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('job_detile', args=[str(self.id)])
