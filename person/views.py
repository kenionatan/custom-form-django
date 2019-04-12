from django.views.generic.edit import CreateView
from .models import Person
from .forms import CreateForm


class NewPerson(CreateView):
    model = Person
    form_class = CreateForm

    def get_form(self):
        form = super().get_form()
        return form

    def form_valid(self, form):
        return super(NewPerson, self).form_valid(form)
