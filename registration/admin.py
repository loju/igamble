from django.contrib import admin

from .models import BonusForLoginModel, BonusForDepositModel


admin.site.register(BonusForLoginModel)
admin.site.register(BonusForDepositModel)
