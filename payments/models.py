
from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration_days = models.IntegerField()

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=False)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="created")
