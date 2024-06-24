from rest_framework import viewsets
from customers.models import Customer, CustomerSubscription
from customers.serializers import (
    # CustomerSerializer,
    CustomerSubscriptionSerializer
)


class CustomerSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CustomerSubscription.objects.filter(is_active=True)
    serializer_class = CustomerSubscriptionSerializer

    def perform_create(self, serializer):
        # setting up the logged-In user instance for the customer
        # for the security purpose
        # serializer.save(customer=self.request.user)
        # hard coding with id 1 for now can be replaced by upper line
        serializer.save(customer=self.request.user)

