from django.db import models
from base.models import UserStampModel


class Subscription(UserStampModel):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )
    code = models.CharField(
        max_length=256,
        unique=True,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    validity = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Enter in Days'
    )
    status = models.BooleanField(
        default=True,
        help_text="True incase of active status"
    )

    def __str__(self):
        return f'{self.name}'
