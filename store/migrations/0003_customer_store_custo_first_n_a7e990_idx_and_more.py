# Generated by Django 5.0.3 on 2024-04-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name', 'last_name'], name='store_custo_first_n_a7e990_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
