from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Bets(TrackingModel):
    event = models.CharField(max_length=255)
    pick = models.CharField(max_length=255)
    odd = models.FloatField()
    start = models.DateTimeField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['start']
