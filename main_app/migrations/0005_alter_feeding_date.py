# Generated by Django 4.2.6 on 2023-10-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_merge_0002_feeding_0003_rename_feed_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding date'),
        ),
    ]