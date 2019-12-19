# Generated by Django 2.2.9 on 2019-12-19 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_one', '0002_auto_20191218_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='WPSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='many_to_one.WPSUser')),
            ],
        ),
    ]
