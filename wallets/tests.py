from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import WalletModel

UserModel = get_user_model()


class WalletModelClassTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='John', password='secret')

    def test_wallet_creation(self):
        wallet = WalletModel(user=self.user, wallet_type='R', value=300)
        self.assertEqual(wallet.value, 300)
        self.assertEqual(wallet.get_wallet_type_display(), 'Real Money EUR')
        self.assertEqual(wallet.user.username, 'John')

    def test_clean(self):
        raise NotImplementedError