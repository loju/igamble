"""
Additional Models for User
"""
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):

    @property
    def has_active_wallet(self):
        return self.get_active_wallet()

    def get_active_wallet(self):
        oldest_real_wallet = self.wallet.oldest_real_not_empty()
        oldest_bonus_wallet = self.wallet.oldest_unused_bonus_not_empty()
        if oldest_real_wallet:
            return oldest_real_wallet
        elif oldest_bonus_wallet:
            return oldest_bonus_wallet
        return False


class BonusModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username


class BonusForLoginModel(BonusModel):
    pass


class BonusForDepositModel(BonusModel):
    threshold = models.PositiveSmallIntegerField(default=0)


class WagerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username
