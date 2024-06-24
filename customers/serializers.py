from rest_framework import serializers
from customers.models import Customer, CustomerSubscription
from subscriptions.serializers import SubscriptionSerializer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ('created_at', 'updated_at',)


class CustomerSubscriptionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = CustomerSubscription
        fields = (
            'customer',
            'subscription',
            'plan_start_datetime',
            'plan_end_datetime',
            'is_active',
            'is_renewal',
        )
