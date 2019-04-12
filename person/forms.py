from django import forms
from person.models import Person


class CreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'col-4'}),
        }
