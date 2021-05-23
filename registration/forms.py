from django import forms
from . import models


class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'division_code_gosb', 'division_code_vsp', 'post')
