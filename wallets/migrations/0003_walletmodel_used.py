# Generated by Django 2.1.4 on 2018-12-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_auto_20181213_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletmodel',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
