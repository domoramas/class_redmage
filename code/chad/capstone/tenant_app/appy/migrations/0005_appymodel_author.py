# Generated by Django 2.1.5 on 2019-01-17 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appy', '0004_auto_20190114_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='appymodel',
            name='author',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
