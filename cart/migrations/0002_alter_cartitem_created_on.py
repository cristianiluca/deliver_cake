# Generated by Django 4.2.11 on 2024-03-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
