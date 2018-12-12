# Generated by Django 2.1.4 on 2018-12-11 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='walletmodel',
            options={'ordering': ['-wallet_type', 'created'], 'verbose_name': 'Wallet', 'verbose_name_plural': 'Wallets'},
        ),
        migrations.AlterField(
            model_name='walletmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='walletmodel',
            name='wallet_type',
            field=models.CharField(choices=[('R', 'Real Money EUR'), ('B', 'Bonus Money BNS')], max_length=1),
        ),
    ]