# Generated by Django 4.2.11 on 2024-03-30 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_deliverdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverdata',
            name='cake_text',
        ),
        migrations.RemoveField(
            model_name='deliverdata',
            name='deliver_date',
        ),
        migrations.RemoveField(
            model_name='deliverdata',
            name='deliver_time',
        ),
    ]