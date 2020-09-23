# Generated by Django 3.0.8 on 2020-09-22 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20200922_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
