from django import forms
from . import models


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'division_code_gosb', 'division_code_vsp', 'post')
