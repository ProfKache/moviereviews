from django.db import models
from apps.helpers.models import TrackingModel


class Movie(TrackingModel):
    """A class representing a table for storing movie info"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movies/images/')
    year = models.PositiveIntegerField('Year Released', blank=True)
    url = models.URLField(blank=True)

    class Meta(TrackingModel.Meta):
        """Extra info about the Movie model"""
