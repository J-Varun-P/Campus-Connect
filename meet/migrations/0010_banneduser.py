# Generated by Django 3.1.7 on 2021-05-02 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meet', '0009_remove_deleted_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banneduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned_a', to='meet.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned_u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]