# Generated by Django 3.1.2 on 2020-11-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20201105_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth',
            field=models.DateField(blank=True, max_length=10, null=True, verbose_name='Data de nascimento'),
        ),
    ]
