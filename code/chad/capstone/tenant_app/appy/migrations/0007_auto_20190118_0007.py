# Generated by Django 2.1.5 on 2019-01-18 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0006_auto_20190117_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appymodel',
            name='author',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
