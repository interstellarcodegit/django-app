# Generated by Django 3.0.8 on 2020-09-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='myproduct', max_length=20),
        ),
    ]
