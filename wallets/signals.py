"""
Signal for deposit action
"""

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DepositModel

UserModel = get_user_model()


def update_wallet(user, bonus):
    oldest_bonus_wallet, created = user.wallet.unused_bonus().get_or_create(
        wallet_type='B', user=user
    )
    oldest_bonus_wallet.update_value(bonus.value)

    return oldest_bonus_wallet, created


@receiver(post_save, sender=DepositModel)
def append_bonus_after_deposit(sender, instance, created, **kwargs):
    """
    :param sender: Deposit class
    :param instance:
    :param created:
    :param kwargs:
    Update wallet after deposit action.
    """
    if created:
        user = instance.user
        # update real wallet
        oldest_real_wallet = user.wallet.oldest_real()
        oldest_real_wallet.update_value(instance.value)

        # assign bonus if any
        bonus = user.bonusfordepositmodel
        if instance.value > bonus.threshold:
            update_wallet(user, bonus)
