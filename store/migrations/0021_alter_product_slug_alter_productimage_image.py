# Generated by Django 5.0.4 on 2025-02-11 08:16

import store.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0020_productimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                upload_to="store/images",
                validators=[store.validators.validate_image_size],
            ),
        ),
    ]
