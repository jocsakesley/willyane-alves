# Generated by Django 3.1.2 on 2021-01-08 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20210108_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='kit',
        ),
        migrations.DeleteModel(
            name='Kit',
        ),
    ]
