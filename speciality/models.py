from django.db import models
from django.contrib.auth.models import User
class Speciality(models.Model):
    spec_name = models.CharField(max_length=100)

    def __str__(self):
        return self.spec_name

