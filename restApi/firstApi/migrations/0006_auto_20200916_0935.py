# Generated by Django 3.0.8 on 2020-09-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApi', '0005_auto_20200916_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
