# Generated by Django 4.0.5 on 2022-08-08 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='label',
            new_name='job_label',
        ),
    ]
