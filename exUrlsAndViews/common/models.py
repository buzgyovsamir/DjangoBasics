from django.db import models


class TimeStampModel(models.Model):
    """
    Abstract base model that provides created_at timestamp.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the record was created"
    )

    class Meta:
        abstract = True