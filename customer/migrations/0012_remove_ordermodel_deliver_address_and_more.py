# Generated by Django 4.2.11 on 2024-03-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_ordermodel_elements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='deliver_address',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='deliver_day',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='deliver_time',
        ),
    ]
