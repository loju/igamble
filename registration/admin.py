from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BonusForLoginModel, BonusForDepositModel, User, WagerModel


admin.site.register(BonusForLoginModel)
admin.site.register(BonusForDepositModel)
admin.site.register(User, UserAdmin)
admin.site.register(WagerModel)
