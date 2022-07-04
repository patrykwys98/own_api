from django.db import models
from .helpers import Bets, TrackingModel


#! Blogabet Models
class BlogabetAuthor(TrackingModel):
    author_name = models.CharField(max_length=255)
    author_yield = models.FloatField()
    author_odds = models.IntegerField()


class BlogabetBets(Bets):
    author = models.ForeignKey(BlogabetAuthor, on_delete=models.CASCADE, null=True, blank=True)
    stake = models.IntegerField()
