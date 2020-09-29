# Generated by Django 3.0.8 on 2020-09-24 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reports', to='Users.Patient'),
        ),
    ]