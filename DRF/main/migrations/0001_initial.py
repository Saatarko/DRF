# Generated by Django 4.2.13 on 2024-06-19 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название банка')),
                ('UNN', models.IntegerField(verbose_name='УНН банка')),
            ],
            options={
                'verbose_name': 'Банки',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=20, verbose_name='Название валюты')),
                ('slug', models.SlugField(max_length=20, verbose_name='Слаг валюты')),
            ],
            options={
                'verbose_name': 'Валюты',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_exchange', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='курс валюты')),
                ('data', models.DateField(verbose_name='дата курса')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bank')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency')),
            ],
            options={
                'verbose_name': 'Курсы валют',
                'verbose_name_plural': 'Курсы валют',
            },
        ),
    ]
