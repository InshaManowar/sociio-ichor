# Generated by Django 3.2.5 on 2021-08-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_agree_donorrequest_i_agree_to_the_terms_and_conditions_stated_below'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorrequest',
            name='date_of_birth',
            field=models.DateField(default=''),
        ),
    ]
