# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User


# Создаём класс формы
class RegistrForm(UserCreationForm):

    lastname = forms.CharField(max_length=80)
    firstname = forms.CharField(max_length=80)
    department_code = forms.CharField(max_length=80)
    post = forms.CharField(max_length=80)
    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('lastname', 'firstname', 'department_code', 'post',)