from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Bank(models.Model):
    name = models.CharField('Название банка', max_length=100)
    UNN = models.IntegerField('УНН банка')

    def __str__(self):
        return f'{self.name}{self.UNN}'

    class Meta:
        verbose_name = 'Банки'
        verbose_name_plural = 'Банки'


class Currency(models.Model):
    currency_name = models.CharField('Название валюты', max_length=20)
    slug = models.SlugField('Слаг валюты', max_length=20)

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = 'Валюты'
        verbose_name_plural = 'Валюты'


class Exchange(models.Model):
    currency_exchange = models.DecimalField('курс валюты', max_digits=10, decimal_places=2)
    date = models.DateField('дата курса')

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.currency_exchange} {self.date}"

    class Meta:
        verbose_name = 'Курсы валют'
        verbose_name_plural = 'Курсы валют'
