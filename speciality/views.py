from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Speciality

@login_required
def spec_list(request):
    specs = Speciality.objects.all()
    return render(request,'speciality/spec.html', {'specs':specs})

