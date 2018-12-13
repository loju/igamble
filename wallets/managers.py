"""
Managers for Wallet models
"""

from django.db import models


class TypeQuerySet(models.QuerySet):
    """
    Querysets for Manager
    """
    def real(self):
        return self.filter(wallet_type='R')

    def bonus(self):
        return self.filter(wallet_type='B')


class WalletManager(models.Manager):
    """
    Manager for Wallet Model
    """
    def get_queryset(self):
        return TypeQuerySet(self.model, using=self._db)

    def real(self):
        return self.get_queryset().real()

    def bonus(self):
        return self.get_queryset().bonus()

    def oldest_real(self):
        return self.real().last()

    def oldest_bonus(self):
        return self.bonus().last()
