import pytest
from django.test import TestCase

from subscriptions.config import SubscriptionConfig
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        SubscriptionConfig.load_fixture_data()

    def test_total_active_subscriptions(self):
        self.assertEqual(
            3,
            Subscription.objects.filter(status=True).count()
        )

    def test_subscription_mapping_check(self):
        subscription = Subscription.objects.get(code='platinum365')
        self.assertEqual(
            499,
            subscription.price
        )
        self.assertEqual(
            365,
            subscription.validity
        )

