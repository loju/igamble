"""
Wallet Models for User
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from .managers import WalletManager

UserModel = get_user_model()


class WalletModel(models.Model):
    """
    Wallet Model class for User
    """

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wallet')
    wallet_type = models.CharField(max_length=1, choices=settings.WALLET_TYPE)
    value = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    objects = WalletManager()

    class Meta:
        ordering = ['-wallet_type', 'created']
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return '{0}: {1}'.format(self.get_wallet_type_display(), self.value)

    # def clean(self):
    #     # TODO: put here validation rules for wallet
    #     raise NotImplementedError
