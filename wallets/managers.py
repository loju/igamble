"""
Managers for Wallet models
"""

from django.db import models


class TypeQuerySet(models.QuerySet):
    """
    Querysets for Manager
    """
    def not_empty(self):
        return self.filter(value__gt=0)

    def unused(self):
        return self.filter(used=False)

    def not_spent(self):
        return self.filter(spent=0)

    def spent(self):
        return self.filter(spent__gt=0)

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

    def unused_bonus(self):
        return self.bonus().unused()

    def oldest_unused_bonus(self):
        return self.unused_bonus().last()

    def oldest_real_not_empty(self):
        return self.real().not_empty().last()

    def oldest_unused_bonus_not_empty(self):
        return self.unused_bonus().not_empty().last()
