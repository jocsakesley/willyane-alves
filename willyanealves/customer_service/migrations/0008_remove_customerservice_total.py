# Generated by Django 3.1.2 on 2020-11-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0007_remove_serviceitem_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='total',
        ),
    ]
