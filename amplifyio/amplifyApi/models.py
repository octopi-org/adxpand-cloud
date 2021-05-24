#models.py
from django.db import models
import sys
import os.path 

# create your models here
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    campaignname = models.CharField(max_length=1000)
    campaignid = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Ben_Tuition(models.Model):
    customer_resource_name = models.CharField(max_length=60)
    
    class Campaign(models.Model):
        campaign_name = models.CharField(max_length=60)
        campaign_id = models.CharField(max_length=60)
    
    class AdGroup(models.Model):
        ad_group_name = models.CharField(max_length=60)
    
    class Metrics(models.Model):
        metrics_clicks = models.CharField(max_length=60)
        metrics_impressions = models.CharField(max_length=60)
        metrics_ctr = models.CharField(max_length=60)
        metrics_cpc = models.CharField(max_length=60)

    def __str__(self):
        return self.customer_resource_name          
