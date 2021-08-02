# Generated by Django 3.2.5 on 2021-07-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('blood_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='a', max_length=20, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=None, max_length=400, unique=True)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-'), ('Hh', 'Hh')], default=None, max_length=20)),
                ('blood_type', models.CharField(choices=[('Whole Blood', 'Whole Blood'), ('Plasma', 'Plasma'), ('Platelets', 'Platelets')], default=None, max_length=50)),
                ('acceptable_blood_group', models.CharField(default=None, max_length=100)),
                ('Phone', models.CharField(default=None, max_length=10)),
                ('units', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'Blood Requests',
            },
        ),
    ]
