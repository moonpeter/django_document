# Generated by Django 3.0 on 2019-12-18 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_one', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Manufacturer',
            new_name='manufacturer',
        ),
    ]