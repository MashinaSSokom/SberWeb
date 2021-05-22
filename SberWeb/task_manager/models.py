from django.db import models

# Create your models here.
class Worker(models.Model):
    lastname = models.CharField(max_length=80, verbose_name='Фамилия')
    firstname = models.CharField(max_length=80, verbose_name='Имя')
    department_code = models.CharField(max_length=80, verbose_name='Код подразделения')
    post = models.CharField(max_length=80, verbose_name='Должность')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ('lastname', 'firstname')

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

class Task(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    creator = models.CharField(max_length=60, verbose_name='Создатель')
    #creator = models.ForeignKey(Worker, on_delete=models.SET_NULL, blank=True, verbose_name='Создатель')
    description = models.TextField(verbose_name='Описание задания')
    date_start = models.DateField(verbose_name="Дата начала подработки", blank=True)
    date_finish = models.DateField(verbose_name="Дата окончания подработки", blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подработка'
        verbose_name_plural = 'Подработки'
        ordering = ('title', 'creator')

    def __str__(self):
        return f'{self.lastname} {self.firstname}'