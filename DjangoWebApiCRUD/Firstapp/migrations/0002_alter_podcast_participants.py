# Generated by Django 3.2 on 2021-04-20 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=models.CharField(max_length=99, null=True, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
