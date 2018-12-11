"""
Additional Models for User
"""

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class BonusModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username


class BonusForLoginModel(BonusModel):
    pass


class BonusForDepositModel(BonusModel):
    threshold = models.PositiveSmallIntegerField(default=0)
