# Generated by Django 3.2.5 on 2021-07-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_bloodrequest_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='note',
            field=models.TextField(default=None, null=True),
        ),
    ]
