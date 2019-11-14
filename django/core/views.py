from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    ListView, DetailView,
)
from core.models import Job, Project
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return {'projects':Project.objects.all(),'jobs':Job.objects.all()}
# class ProjectList(ListView):
#     model = Project

class ProjectDetail(DetailView):
    model = Project

class JobList(ListView):
    model = Job

class JobDetail(DetailView):
    model = Job
