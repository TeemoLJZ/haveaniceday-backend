# Generated by Django 4.2.4 on 2023-09-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_alter_illustration_del_time_alter_illustration_illu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illustration',
            name='del_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]