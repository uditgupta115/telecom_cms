from datetime import timedelta

from django.db import models
from django.utils import timezone
from base.models import DateTimeStampModel
from base.enums import GenderEnum
from subscriptions.models import Subscription


class Customer(DateTimeStampModel):
    name = models.CharField(max_length=256, null=False, blank=False)
    gender = models.CharField(max_length=8, null=True, blank=True, choices=GenderEnum.choices())
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    aadhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(null=False, default=timezone.now)
    mobile_number = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CustomerSubscription(DateTimeStampModel):
    subscription = models.ForeignKey(
        to=Subscription,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    plan_start_datetime = models.DateTimeField(
        null=False,
        blank=False,
        db_index=True
    )
    plan_end_datetime = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True
    )
    is_active = models.BooleanField(default=True)
    is_renewal = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer_id} - {self.subscription_id}'

    def clean(self):
        if not self.pk:
            existing_dataset = self.__class__.objects.filter(
                customer=self.customer,
                subscription=self.subscription,
                is_active=True,
            )
            if existing_dataset.exists():
                self.is_renewal = True
                last_record = existing_dataset.order_by('plan_end_datetime').last()
                self.plan_start_datetime = last_record.plan_end_datetime + timedelta(days=1)
                self.plan_end_datetime = last_record.calculate_subscription_end_datetime()

        if self.plan_end_datetime != self.calculate_subscription_end_datetime():
            raise ValidationError("Plan end date is not as per Subscription End datetime")

    def save(self, *args, **kwargs):
        new_plan = self.pk is None
        if not self.plan_end_datetime and self.plan_start_datetime:
            self.plan_end_datetime = self.calculate_subscription_end_datetime()
        super().save(*args, **kwargs)
        if new_plan:
            # once new plan activated, disable the old plan
            existing_dataset = self.__class__.objects.filter(
                customer=self.customer,
                subscription=self.subscription,
                is_active=True,
                plan_end_datetime__gte=self.plan_start_datetime,
            ).exclude(pk=self.pk)
            if existing_dataset.exists():
                existing_dataset.update(is_active=False)

    def calculate_subscription_end_datetime(self):
        return self.plan_start_datetime + timedelta(
            days=self.subscription.validity
        )
