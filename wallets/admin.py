from django.contrib import admin

from .models import DepositModel, WalletModel

admin.site.register(DepositModel)
admin.site.register(WalletModel)
