from django.test import Client, TestCase
from django.contrib.auth import get_user_model

from .models import WalletModel

UserModel = get_user_model()


class WalletModelClassTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='John', password='secret')

    def test_wallet_object_creation(self):
        wallet = WalletModel(user=self.user, wallet_type='R', value=300)
        self.assertEqual(wallet.value, 300)
        self.assertEqual(wallet.get_wallet_type_display(), 'Real Money EUR')
        self.assertEqual(wallet.user.username, 'John')


class WalletSignalsTest(TestCase):

    def test_creation_wallets_when_user_is_created(self):
        user = UserModel.objects.create_user(username='Jon', password='secret')
        self.assertEqual(WalletModel.objects.filter(user=user).count(), 2)
        self.assertEqual(WalletModel.objects.filter(user=user).real().count(), 1)
        self.assertEqual(WalletModel.objects.filter(user=user).bonus().count(), 1)


class WallerManagersTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='John', password='secret')
        cls.wallet_real_1 = WalletModel.objects.create(user=cls.user, wallet_type='R', value=300)
        cls.wallet_real_2 = WalletModel.objects.create(user=cls.user, wallet_type='R', value=300)
        cls.wallet_bonus_1 = WalletModel.objects.create(user=cls.user, wallet_type='B', value=300)
        cls.wallet_bonus_2 = WalletModel.objects.create(user=cls.user, wallet_type='B', value=300)
        cls.wallet_bonus_3 = WalletModel.objects.create(user=cls.user, wallet_type='B', value=300)

    def test_amount_of_real_wallets(self):
        """
        check against 3 wallets, because one was created curing user creation
        """
        self.assertEqual(self.user.wallet.real().count(), 3)

    def test_amount_of_bonus_wallets(self):
        """
        check against 4 wallets, because one was created curing user creation
        """
        self.assertEqual(self.user.wallet.bonus().count(), 4)
