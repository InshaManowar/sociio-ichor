# Generated by Django 3.2.5 on 2021-07-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_bloodrequest_acceptable_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='acceptable_blood_group',
            field=models.CharField(default='AB+', max_length=100, null=True),
        ),
    ]
