# Generated by Django 3.1.5 on 2021-01-14 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20210114_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='master',
        ),
        migrations.AddField(
            model_name='master',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='service.service'),
        ),
    ]
