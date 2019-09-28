from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FibonacciTest(models.Model):
    latency = models.CharField(max_length=100)
    numeric = models.PositiveIntegerField(blank=True,null=True)
    output = models.PositiveIntegerField(blank=True,null=True)

def __str__(self):
    return self.Latency
