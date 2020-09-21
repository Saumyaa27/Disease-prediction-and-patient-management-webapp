# Generated by Django 3.0.8 on 2020-09-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Address',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default=None, max_length=80, null=True),
        ),
    ]
