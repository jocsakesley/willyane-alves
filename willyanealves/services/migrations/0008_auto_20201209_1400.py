# Generated by Django 3.1.2 on 2020-12-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20201209_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor'),
        ),
    ]
