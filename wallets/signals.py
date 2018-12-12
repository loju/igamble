"""
Signal for deposit action
"""

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    if created:
        user = instance.user
        bonus = user.bonusfordepositmodel
        if instance.value > bonus.threshold:
            oldest_bonus_wallet = user.wallet.bonus().last()
            oldest_bonus_wallet.value += bonus.value
            oldest_bonus_wallet.save()
