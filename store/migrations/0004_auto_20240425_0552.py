# Generated by Django 5.0.4 on 2024-04-25 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_store_custo_first_n_a7e990_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO store_collection (title)
            VALUES ("COLLECTION 1")
            """,
            """
            DELETE FROM store_collection 
            WHERE title = "COLLECTION 1"
             """
        )
    ]
