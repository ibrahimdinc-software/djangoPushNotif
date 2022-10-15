from django.db import models
from django.core.exceptions import FieldError
from django.conf import settings

# Create your models here.



class SubscriptionInfo(models.Model):
    browser = models.CharField(max_length=100)
    endpoint = models.URLField(max_length=500)
    auth = models.CharField(max_length=100)
    p256dh = models.CharField(max_length=100)


class PushInformation(models.Model):
    user = models.ForeignKey("pushuser.pushusermodel", related_name='webpush_info', on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionInfo, related_name='webpush_info', on_delete=models.CASCADE)


