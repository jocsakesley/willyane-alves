# Generated by Django 3.1.2 on 2020-11-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20201106_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='pictures/%Y/%m/', verbose_name='Foto'),
        ),
    ]
