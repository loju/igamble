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
