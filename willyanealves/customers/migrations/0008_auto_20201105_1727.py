# Generated by Django 3.1.2 on 2020-11-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20201105_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth',
            field=models.DateField(blank=True, max_length=10, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(blank=True, max_length=255, verbose_name='Bairro'),
        ),
    ]
