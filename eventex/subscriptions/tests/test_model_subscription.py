from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name='Maurício Fagundes',
            cpf='12345678901',
            email='mauricio.fagundes@gmail.com',
            phone='21-99811-9570'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Maurício Fagundes', str(self.obj))

    def test_paid_default_to_false(self):
        """By default must be false"""
        self.assertEqual(False, self.obj.paid)