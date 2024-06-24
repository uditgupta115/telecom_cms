import pytest
from datetime import timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from base.enums import GenderEnum
from customers.models import Customer, CustomerSubscription
from subscriptions.models import Subscription
from subscriptions.config import SubscriptionConfig


class CustomerModelTest(TestCase):

    def setUp(self):
        Customer.objects.create(
            name="John Doe", dob="1990-01-01", email="john@example.com",
            aadhar_number="123456789012", mobile_number="9876543210",
            gender=GenderEnum.MALE.name
        )
        # self.client = Client()
        SubscriptionConfig.load_fixture_data()

    def test_customer_creation(self):
        john = Customer.objects.get(name="John Doe")
        self.assertEqual(john.email, "john@example.com")

    def test_create_subscription_customer(self):
        john = Customer.objects.get(name="John Doe")
        subscription = Subscription.objects.get(code='platinum365')

        plan_start_datetime = timezone.now()
        cs = CustomerSubscription.objects.create(
            customer=john,
            subscription=subscription,
            plan_start_datetime=plan_start_datetime
        )
        assert type(cs.id) == int
        return cs.id

    def test_validate_subscription_customer_plan_end_date(self):
        john = Customer.objects.get(name="John Doe")
        subscription = Subscription.objects.get(code='platinum365')

        plan_start_datetime = timezone.now()
        cs_id = self.test_create_subscription_customer()

        cs_instance = CustomerSubscription.objects.get(id=cs_id)
        self.assertEqual(
            cs_instance.plan_end_datetime,
            plan_start_datetime + timedelta(days=subscription.validity)
        )
