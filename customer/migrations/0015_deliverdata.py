# Generated by Django 4.2.11 on 2024-03-30 17:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_customerdata_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliverData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_date', models.DateField(default=datetime.date.today)),
                ('deliver_time', models.TimeField()),
                ('cake_text', models.TextField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=15)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.ordermodel')),
            ],
        ),
    ]