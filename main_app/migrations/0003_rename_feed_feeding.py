# Generated by Django 4.2.6 on 2023-10-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feed',
            new_name='Feeding',
        ),
    ]
