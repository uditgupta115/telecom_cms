from django.contrib import admin
from customers.models import Customer, CustomerSubscription


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active')
    search_fields = ('name', 'email',)


@admin.register(CustomerSubscription)
class CustomerSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'subscription_name',
        'plan_start_datetime',
        'plan_end_datetime',
        'is_active',
        'is_renewal',
    )
    autocomplete_fields = ('customer',)
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('customer', 'subscription')

    def subscription_name(self, instance):
        return f'{instance.subscription.name}'

    def customer_name(self, instance):
        return f'{instance.customer.name}'
