from django.db import models
from helpers.models import TrackingModel


class Bets(TrackingModel):
    bet_type = models.CharField(max_length=20)
    bet_amount = models.IntegerField()
    bet_result = models.IntegerField()
    bet_status = models.CharField(max_length=20)
    bet_result_amount = models.IntegerField()
    bet_result_status = models.CharField(max_length=20)
