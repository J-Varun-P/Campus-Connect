# Generated by Django 3.1.7 on 2021-04-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0005_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joining',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_activities', to='meet.activity'),
        ),
    ]
