# Generated by Django 5.0.1 on 2024-01-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_remove_userreviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviews',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
