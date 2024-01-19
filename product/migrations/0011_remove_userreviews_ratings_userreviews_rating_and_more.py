# Generated by Django 5.0.1 on 2024-01-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_product_quantity_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreviews',
            name='ratings',
        ),
        migrations.AddField(
            model_name='userreviews',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
