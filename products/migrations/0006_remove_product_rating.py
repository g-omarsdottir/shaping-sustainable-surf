# Generated by Django 5.0.6 on 2024-07-08 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_product_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="rating",
        ),
    ]
