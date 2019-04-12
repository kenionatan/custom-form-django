from django.urls import path
from .views import NewPerson

urlpatterns = [
    path('', NewPerson.as_view(), name="new_person")
]
