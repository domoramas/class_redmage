# Generated by Django 2.1.4 on 2019-01-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gl_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylistmodel',
            name='gc_submit_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
