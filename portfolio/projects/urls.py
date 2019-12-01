
from django.urls import path,re_path
from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("projects/", views.index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
]