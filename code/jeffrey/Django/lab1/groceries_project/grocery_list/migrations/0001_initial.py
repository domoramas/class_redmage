# Generated by Django 2.1.4 on 2019-01-08 21:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(verbose_name='date_created')),
                ('completed_date', models.DateTimeField(verbose_name='date completed')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name=django.core.validators.MaxValueValidator(10))),
                ('in_basket', models.BooleanField(default=False)),
            ],
        ),
    ]
