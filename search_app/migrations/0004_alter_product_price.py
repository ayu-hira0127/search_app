# Generated by Django 3.2.25 on 2024-10-12 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0003_auto_20241011_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
