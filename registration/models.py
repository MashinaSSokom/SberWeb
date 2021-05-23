from django.contrib.auth.models import AbstractUser
from django.db import models

division_code_gosb_choices = [
    ('4157', '4157',),
    ('9070', '9070',),
    ('8635', '8635',),
    ('8636', '8636',),
    ('8567', '8567',),
    ('8645', '8645',),
    ('8557', '8557',),
    ('8556', '8556',)
]

post_choices = [
    ('СМО', 'Старший менеджер по обслуживанию'),
    ('ВМО', 'Ведущий менеджер по обслуживанию'),
    ('МО', 'Менеджер по обслуживанию'),
    ('СКМ', 'Старший клиентский менеджер'),
    ('КМ', 'Клиентский менеджер'),
    ('К', 'Консультант')
]


class CustomUser(AbstractUser):
    division_code_gosb = models.CharField(max_length=400, choices=division_code_gosb_choices,
                                          verbose_name='ГОСБ')
    division_code_vsp = models.CharField(max_length=400, verbose_name='ВСП')
    post = models.TextField(choices=post_choices, verbose_name='Должность')
    password_str = models.CharField(max_length=50, verbose_name='Пароль в текстовом виде (для разработки)')
