from django.contrib import admin
from subscriptions.models import Subscription


@admin.register
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = ('id', 'name', 'price', 'validity', 'status')
    readonly_fields = ('created_by', 'updated_by')
