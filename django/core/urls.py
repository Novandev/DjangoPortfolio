from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # path('projects',
    #      views.ProjectList.as_view(),
    #      name='ProjectList'),
    path('', views.IndexView.as_view(), name='index'),
    path('projects/<int:pk>',
        views.ProjectDetail.as_view(),
        name='ProjectDetail'),
    path('jobs/<int:pk>',
        views.JobDetail.as_view(),
        name='JobDetail'),
]