# Generated by Django 3.1.2 on 2021-01-08 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20210108_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='stock_item',
        ),
    ]
