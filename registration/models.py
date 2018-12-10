from django.contrib.auth.signals import user_logged_in


def append_bonus_after_login(sender, user, request, **kwargs):
    pass


user_logged_in.connect(append_bonus_after_login)
