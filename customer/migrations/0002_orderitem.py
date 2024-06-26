# Generated by Django 4.2.7 on 2024-03-23 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.menuitem')),
            ],
        ),
    ]
