from rest_framework import serializers
from .models import BenMetrics, BenAdGroup, BenCampaign

class BenCampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BenCampaign
        fields = ('id', 'customer_resource_name', 'campaign_name', 
        'campaign_id')

class BenAdGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BenAdGroup
        fields = ('id', 'customer_resource_name', 'campaign_name', 
        'campaign_id', 'ad_group_name')

class BenMetricsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BenMetrics
        fields = ('id', 'customer_resource_name', 'campaign_name', 
        'campaign_id', 'ad_group_name', 'metrics_clicks', 'metrics_impressions', 
        'metrics_ctr', 'metrics_cpc', 'datepulled')

#might need this when we change model type
#class Ben_TuitionSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
       # model = Ben_Tuition
        #fields = ('id', 'customer_resource_name', 'campaign_name', 
        #'campaign_id', 'ad_group_name', 'metrics_clicks', 'metrics_impressions', 
        #'metrics_ctr', 'metrics_cpc')