# serializers.py
from rest_framework import serializers

from .models import Hero, Ben_Tuition

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias', 'campaign_name', 'campaign_id')

class Ben_TuitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ben_Tuition
        fields = ('id', 'customer_resource_name', 'campaign_name', 
        'campaign_id', 'ad_group_name', 'metrics_clicks', 'metrics_impressions', 
        'metrics_ctr', 'metrics_cpc')