from django.shortcuts import render
from projects.models import Project
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    # template_name = 'project_index.html'
    def get(self, request):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request, 'home.html', context)
# Create your views here.


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request,pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project':project
    }
    return render(request,'project_detail.html',context)