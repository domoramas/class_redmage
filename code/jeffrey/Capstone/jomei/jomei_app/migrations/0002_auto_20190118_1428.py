# Generated by Django 2.1.5 on 2019-01-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jomei_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='userlocationpoint',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date_created'),
        ),
    ]
