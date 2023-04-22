from django.db import models

class CardDetails(models.Model):
    card_id = models.CharField(max_length=15, primary_key=True)
    card_holder_name = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
