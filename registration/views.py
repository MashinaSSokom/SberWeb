
from django.shortcuts import render

from . import forms


def registration(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.username = 'test_1'
            new_user.set_password('1234')
            new_user.save()
            return render(request, 'user_info.html', {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})
