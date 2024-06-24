from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.viewsets import CustomerSubscriptionViewSet

router = DefaultRouter()
router.register(
    r'customer-subscription',
    CustomerSubscriptionViewSet,
    basename='customer_subscription'
)

urlpatterns = [
    path('', include(router.urls)),
]
