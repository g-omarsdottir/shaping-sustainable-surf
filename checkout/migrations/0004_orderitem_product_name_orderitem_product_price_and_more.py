# Generated by Django 5.0.6 on 2024-07-03 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0003_alter_order_discount_code_delete_discountcode"),
        ("products", "0004_alter_subcategory_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="product_name",
            field=models.CharField(default="Unknown Product", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderitem",
            name="product_price",
            field=models.DecimalField(
                decimal_places=2, default=0.00, max_digits=6
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.product",
            ),
        ),
    ]
