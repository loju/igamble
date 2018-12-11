from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import BonusForLoginModel, BonusForDepositModel

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_creation_handler(sender, instance, created, **kwargs):
    """
    :param sender: user model class
    :param instance: user object
    :param kwargs:
    Signal creates:
     - two wallets for initial purposes - one with real money
       and additional one with bonus.
     - records for bonuses (login and deposit)

    """
    if created:
        # wallets creation
        for wallet_type in settings.WALLET_TYPE:
            instance.wallet.create(wallet_type=wallet_type[0])

        # bonuses creation (consider annyoing library use)
        BonusForLoginModel.objects.create(user=instance, value=100)
        BonusForDepositModel.objects.create(user=instance, value=20, threshold=100)


def append_bonus_after_login(sender, user, request, **kwargs):
    """
    :param sender: user login view
    :param user: logged user
    :param request:
    :param kwargs:
    Within every user login value from BonusForLoginModel will be added to user wallet
    """
    oldest_real_wallet = user.wallet.filter(wallet_type='R').last()
    bonus_login_value = user.bonusforloginmodel.value
    oldest_real_wallet.value += bonus_login_value
    oldest_real_wallet.save()


user_logged_in.connect(append_bonus_after_login)
