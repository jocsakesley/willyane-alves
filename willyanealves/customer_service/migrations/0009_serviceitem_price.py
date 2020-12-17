# Generated by Django 3.1.2 on 2020-11-14 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('customer_service', '0008_remove_customerservice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_item', to='services.service'),
        ),
    ]
