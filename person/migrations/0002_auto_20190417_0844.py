# Generated by Django 2.2 on 2019-04-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default='01/01/1995'),
        ),
    ]
