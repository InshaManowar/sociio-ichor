# Generated by Django 3.2.5 on 2021-08-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_bloodrequest_urgent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodrequest',
            name='urgent',
        ),
    ]
