# Generated by Django 4.0.5 on 2022-08-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_delete_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_product_price',
            field=models.FloatField(default=0),
        ),
    ]
