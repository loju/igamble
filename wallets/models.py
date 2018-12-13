"""
Wallet Models for User
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinValueValidator

from .managers import WalletManager

UserModel = get_user_model()


class TimeStampedValueModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    value = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1)])

    class Meta:
        abstract = True


class WalletModel(TimeStampedValueModel):
    """
    Wallet Model class for User
    """

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wallet')
    wallet_type = models.CharField(max_length=1, choices=settings.WALLET_TYPE)

    objects = WalletManager()

    class Meta:
        ordering = ['-wallet_type', 'created']
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return '{0}: {1}'.format(self.get_wallet_type_display(), self.value)

    def update_value(self, value):
        self.value += value
        self.save()


class DepositModel(TimeStampedValueModel):
    """
    Deposit class for registering deposits
    """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='deposit')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'

    def __str__(self):
        return 'on: {0} value:{1}'.format(self.created, self.value)
