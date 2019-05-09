from django.db import models
from localflavor.us.models import USStateField


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    birth_date = models.DateField(blank=False, null=False, default="01/01/1995")
    address = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = USStateField(default="AL")

    def __str__(self):
        return self.full_name
