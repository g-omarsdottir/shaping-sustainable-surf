# Generated by Django 5.0.6 on 2024-09-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_newsletter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Save as Draft"),
                    ("finalized", "Save as Finalized Version"),
                    ("send", "Save and Send Newsletter Now"),
                ],
                default="Draft",
                max_length=20,
            ),
        ),
    ]
