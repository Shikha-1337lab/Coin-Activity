# Generated by Django 2.0.2 on 2018-08-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_auto_20180808_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='coin_price',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
        migrations.AlterField(
            model_name='coins',
            name='coin_volume',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
        migrations.AlterField(
            model_name='coins',
            name='market_cap',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
    ]
