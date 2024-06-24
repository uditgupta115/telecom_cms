from django.db import models
from django.contrib.auth.models import User


class DateTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserStampModel(DateTimeStampModel):
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='+'
    )
    updated_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='+'
    )

    class Meta:
        abstract = True
