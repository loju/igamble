from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_creation_handler(sender, instance, **kwargs):
    print(instance)


def append_bonus_after_login(sender, user, request, **kwargs):
    print(user)


user_logged_in.connect(append_bonus_after_login)
