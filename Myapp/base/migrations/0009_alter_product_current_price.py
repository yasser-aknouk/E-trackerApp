# Generated by Django 4.0.5 on 2022-08-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_product_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.FloatField(blank=True),
        ),
    ]
