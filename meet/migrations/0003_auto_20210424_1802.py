# Generated by Django 3.1.7 on 2021-04-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_auto_20210424_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='Say Something about yourself!'),
        ),
    ]