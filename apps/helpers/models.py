import uuid
from django.db import models


class TrackingModel(models.Model):
    """
    A base class that is inherited by all the models with common fields
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
