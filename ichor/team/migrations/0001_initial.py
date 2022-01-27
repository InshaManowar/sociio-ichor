# Generated by Django 3.2.5 on 2022-01-26 05:27

from django.db import migrations, models
import team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('position', models.CharField(default='', max_length=50)),
                ('linkedIn', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=team.models.upload_location)),
            ],
        ),
    ]
