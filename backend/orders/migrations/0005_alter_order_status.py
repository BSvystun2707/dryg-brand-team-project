# Generated by Django 5.0 on 2023-12-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0004_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("awaiting payment", "Awaiting Payment"),
                    ("payment received", "Payment Received"),
                    ("shipped", "Shipped"),
                    ("completed", "Completed"),
                    ("refunded", "Refunded"),
                    ("canceled", "Canceled"),
                    ("failed", "Failed"),
                ],
                default="awaiting payment",
                max_length=63,
            ),
        ),
    ]
