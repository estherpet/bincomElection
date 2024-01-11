# Create your models here.
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)


class LGA(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Ward(models.Model):
    name = models.CharField(max_length=50)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)


class PollingUnit(models.Model):
    name = models.CharField(max_length=50)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)


class AnnouncedPuResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party = models.CharField(max_length=50)
    score = models.IntegerField()

    class Meta:
        app_label = 'election_results'
