"""
Forms for wallets models
"""

from django.forms import ModelForm

from .models import DepositModel


class DepositForm(ModelForm):

    class Meta:
        model = DepositModel
        fields = ['value']

    def save(self, commit=True):
        self.instance.user = self.request.user
        return super().save(commit=commit)
