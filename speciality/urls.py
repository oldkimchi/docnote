from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Speciality

app_name = 'speciality'

urlpatterns = [
    path('', spec_list,name='spec_list'),
    path('detail/<int:pk>',DetailView.as_view(model=Speciality,template_name='speciality/spec.html'), name='spec_detail'),
]