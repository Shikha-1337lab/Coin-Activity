# Generated by Django 2.0.2 on 2018-08-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('symbol', models.TextField()),
                ('coin_type', models.TextField()),
                ('url', models.TextField()),
                ('icon', models.ImageField(upload_to='images/')),
                ('coin_price', models.DecimalField(decimal_places=100, max_digits=100)),
                ('coin_volume', models.DecimalField(decimal_places=100, max_digits=100)),
                ('market_cap', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
    ]
