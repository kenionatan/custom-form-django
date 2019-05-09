from django import forms
from person.models import Person


class CreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'email', 'birth_date', 'state']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'example@mail.com'}),
            'birth_date': forms.TextInput(attrs={'data-mask': '00/00/0000'})
        }
