from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models
from . import forms

from django.contrib.auth import login


def registration(request):
    if request.user.is_authenticated:
        return redirect('user_info')

    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            users_count = models.CustomUser.objects.last().id
            new_user.username = f'user_{new_user.division_code_gosb}_{new_user.division_code_vsp}_{users_count + 1}'
            password = models.CustomUser.objects.make_random_password(16)
            new_user.set_password(password)
            new_user.password_str = password
            new_user.save()

            login(request, new_user)

            return redirect('user_info')
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})


@login_required
def user_info(request):
    password = request.user.password_str
    return render(request, 'user_info.html', {'user': request.user, 'user_password': password})
