# Generated by Django 4.1.7 on 2023-03-12 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_characteristics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristics',
        ),
    ]