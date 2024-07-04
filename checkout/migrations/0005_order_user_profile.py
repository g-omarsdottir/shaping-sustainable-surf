# Generated by Django 5.0.6 on 2024-07-04 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0004_orderitem_product_name_orderitem_product_price_and_more"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="profiles.userprofile",
            ),
        ),
    ]
