# Generated by Django 5.0.1 on 2024-02-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0005_orders_address_orders_status_alter_orders_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]