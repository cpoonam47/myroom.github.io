# Generated by Django 2.0.4 on 2018-05-19 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myrmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ownerreg',
            name='status',
        ),
    ]
