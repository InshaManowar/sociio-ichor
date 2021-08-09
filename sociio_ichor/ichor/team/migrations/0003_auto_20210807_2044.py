# Generated by Django 3.2.5 on 2021-08-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210807_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedIn',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]