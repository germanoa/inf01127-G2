from django.db import models
from django.contrib.auth.models import User

class IP(models.Model):
    address = models.IntegerField(default=0)
    mask = models.IntegerField(default=0)
    version = models.IntegerField(default=4)

class Network(IP):
    name = models.CharField(max_length=256)
    administrator = models.ForeignKey(User, null=True)
    subnets = models.ManyToManyField('self', null=True)
    ips = models.ManyToManyField(IP, related_name="ips")

