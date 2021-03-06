# Generated by Django 3.1.2 on 2020-12-07 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_service', '0035_auto_20201204_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='user',
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Usuário'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(0, '0%'), (5, '5%'), (10, '10%'), (15, '15%'), (20, '20%')], verbose_name='Desconto'),
        ),
    ]
