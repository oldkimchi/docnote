from django.contrib import admin

from .models import Speciality


class specAdmin(admin.ModelAdmin):
    search_fields = ['text','created']

admin.site.register(Speciality)
