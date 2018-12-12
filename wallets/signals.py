"""
Signal for deposit action
"""

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# consider to move below class to separate module or in current
from registration.models import BonusForDepositModel

from .models import DepositModel


UserModel = get_user_model()

@receiver(post_save, sender=DepositModel)
def append_bonus_after_deposit(sender, instance, created, **kwargs):
    """
    :param sender: Deposit class
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    print(instance.user)
