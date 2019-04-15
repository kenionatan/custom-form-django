from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    birth_date = models.DateField(blank=False, null=False, default="1995-01-01")

    def __str__(self):
        return self.full_name
