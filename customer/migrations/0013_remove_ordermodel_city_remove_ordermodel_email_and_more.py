# Generated by Django 4.2.11 on 2024-03-29 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_remove_ordermodel_deliver_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='street',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='zip_code',
        ),
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=15)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.ordermodel')),
            ],
        ),
    ]
