# Generated by Django 3.2.25 on 2024-10-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]