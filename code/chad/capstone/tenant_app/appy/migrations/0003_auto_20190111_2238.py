# Generated by Django 2.1.5 on 2019-01-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_auto_20190111_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appymodel',
            name='current_employer_phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appymodel',
            name='current_employer_zip',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appymodel',
            name='previous_employer_phone',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='appymodel',
            name='previous_employer_zip',
            field=models.CharField(max_length=5),
        ),
    ]
