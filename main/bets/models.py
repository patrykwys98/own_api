from django.db import models
from .helpers import Bets, TrackingModel


#! Blogabet Models
class BlogabetAuthor(TrackingModel):
    author_name = models.CharField(max_length=255)
    author_yield = models.FloatField()
    author_odds = models.IntegerField()

    def __str__(self):
        return self.author_name + ' ' + str(self.author_yield) + ' ' + str(self.author_odds)

class Dyscipline(TrackingModel):
    dyscipline_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.dyscipline_name


class BlogabetBets(Bets):
    author = models.ForeignKey(BlogabetAuthor, on_delete=models.CASCADE, null=True, blank=True)
    dyscipline = models.ForeignKey(Dyscipline, on_delete=models.CASCADE, null=True, blank=True)
    stake = models.IntegerField()

    def __str__(self):
        return self.event + ' ' + self.pick + ' ' + str(self.odd) + ' ' + str(self.start) + ' ' + str(self.author) + ' ' + str(self.dyscipline) + ' ' + str(self.stake)
