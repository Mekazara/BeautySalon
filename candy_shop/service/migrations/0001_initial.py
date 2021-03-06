# Generated by Django 3.1.5 on 2021-01-14 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('expierence', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.master')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('I level', 'I level'), ('II level', 'II level'), ('III level', 'III level')], max_length=30)),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.master')),
            ],
        ),
    ]
