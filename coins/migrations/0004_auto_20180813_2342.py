# Generated by Django 2.0.2 on 2018-08-13 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_auto_20180813_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='coin_price',
            field=models.DecimalField(decimal_places=5, max_digits=40),
        ),
        migrations.AlterField(
            model_name='coins',
            name='coin_volume',
            field=models.DecimalField(decimal_places=5, max_digits=40),
        ),
        migrations.AlterField(
            model_name='coins',
            name='market_cap',
            field=models.DecimalField(decimal_places=5, max_digits=40),
        ),
    ]