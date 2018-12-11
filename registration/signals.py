from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_creation_handler(sender, instance, created, **kwargs):
    """
    :param sender: user model class
    :param instance: user object
    :param kwargs:
    Signal creates two wallets for initial purposes - one with real money
    and additional one with bonus
    """
    if created:
        for wallet_type in settings.WALLET_TYPE:
            instance.wallet.create(wallet_type=wallet_type[0])


def append_bonus_after_login(sender, user, request, **kwargs):
    print(user)


user_logged_in.connect(append_bonus_after_login)
