# Generated by Django 3.1.5 on 2021-01-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20210114_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='certificates',
        ),
        migrations.AddField(
            model_name='certificate',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, related_name='certificate', to='service.master'),
        ),
    ]
