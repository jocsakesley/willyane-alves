# Generated by Django 3.1.2 on 2020-11-16 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0017_auto_20201116_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='serviceitem',
        ),
    ]
