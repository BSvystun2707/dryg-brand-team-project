# Generated by Django 5.0 on 2024-01-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_item_slug"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="wishlist",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="wishlist", to="products.product"
            ),
        ),
    ]
