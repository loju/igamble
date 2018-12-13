"""
Additional Models for User
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


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
