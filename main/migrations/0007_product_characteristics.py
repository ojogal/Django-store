# Generated by Django 4.1.7 on 2023-03-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_product_characteristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]