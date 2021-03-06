"""
Wallet Models for User
"""
import random
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

from .contextmanagers import object_saver
from .managers import WalletManager

UserModel = get_user_model()


def transfer_money(bonus_wallet, real_wallet):
    """
    transfer money from Bonus wallet to Real
    """
    if not bonus_wallet and not real_wallet:
        return
    with object_saver(real_wallet):
        real_wallet.value += bonus_wallet.value

    with object_saver(bonus_wallet):
        bonus_wallet.value = 0


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
    spent = models.PositiveSmallIntegerField(default=0)
    used = models.BooleanField(default=False)

    objects = WalletManager()

    class Meta:
        ordering = ['-wallet_type', '-created']
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return '{0}: {1}'.format(self.get_wallet_type_display(), self.value)

    def update_value(self, value):
        with object_saver(self):
            self.value += value
            if self.value <= 0:
                self.value = 0

    def update_spent(self, value):
        with object_saver(self):
            self.spent += value

    def has_spent(self):
        if self.spent > 0:
            return True
        return False

    def set_used(self):
        with object_saver(self):
            self.used = True

    def update_wallet(self, value):
        self.update_value(value)
        self.update_spent(abs(value))

    def is_empty(self):
        if self.value > 0:
            return False
        return True

    def spin(self):
        # consider to separate this method
        if not self.is_empty():
            choice = bool(random.getrandbits(1))
            if choice:
                self.update_wallet(settings.BET_VALUE)
            else:
                self.update_wallet(settings.BET_VALUE * -1)


class DepositModel(TimeStampedValueModel):
    """
    Deposit class for registering deposits
    """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='deposit')
    wallet = models.ForeignKey(WalletModel, on_delete=models.CASCADE, related_name='wallet_deposit')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'

    def __str__(self):
        return 'on: {0} value:{1}'.format(self.created, self.value)
