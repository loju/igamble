from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from .models import BonusForLoginModel, BonusForDepositModel

UserModel = get_user_model()


class WalletBonusModelClassTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='John', password='secret')

    def test_adding_bonus_after_login(self):
        _client = Client()
        _client.login(username='John', password='secret')
        self.assertTrue(BonusForLoginModel.objects.get(user=self.user))
        self.assertTrue(BonusForDepositModel.objects.get(user=self.user))
