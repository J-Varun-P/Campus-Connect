# Generated by Django 3.1.7 on 2021-04-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='Say Something about yourself!', max_length=150),
        ),
    ]
