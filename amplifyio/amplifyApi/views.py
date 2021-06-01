# views.py
from django.db.models.fields import DateField
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from datetime import datetime
from rest_framework import status
from .serializers import HeroSerializer, BenAdGroupSerializer, BenCampaignSerializer, BenMetricsSerializer
from .models import Hero, BenCampaign, BenAdGroup, BenMetrics

from django.shortcuts import render

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import DetailView
import sys
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

def djangoGAC(client, customer_id):
    ga_service = client.get_service("GoogleAdsService", version="v6")

    query = """
    SELECT ad_group.name, metrics.average_cpc, metrics.clicks, 
    metrics.ctr, metrics.impressions, campaign.id, campaign.name, 
    customer.resource_name, segments.date
    FROM ad_group 
    WHERE segments.date DURING LAST_30_DAYS """

    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id=customer_id , query=query)

    try:
        for batch in response:
            for row in batch.results:  
                BenMetrics.objects.create( customer_resource_name = str(row.customer.resource_name), 
                campaign_name = str(row.campaign.name), campaign_id = str(row.campaign.id), 
                ad_group_name = str(row.ad_group.name), metrics_clicks = str(row.metrics.clicks),
                metrics_impressions = str(row.metrics.impressions), metrics_ctr = str(row.metrics.ctr),
                metrics_cpc = str(row.metrics.average_cpc), datepulled=str(row.segments.date))            

                #BenCampaign.objects.create(customer_resource_name = str(row.customer.resource_name), 
                #

    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)

#class Ben_TuitionViewSet(viewsets.ModelViewSet):
    #google_ads_client = GoogleAdsClient.load_from_storage("C:\\Users\\Shjon\\Documents\\codingprojects\\gittut\\secret\\google-ads.yaml")
    #djangoGAC(google_ads_client, "1255132966")
    #queryset = Ben_Tuition.objects.all().order_by['campaign_name']
    #serializer_class = Ben_TuitionSerializer

class BenCampaignViewSet(viewsets.ModelViewSet):
    #BenMetrics.objects.all().delete()
    queryset = BenCampaign.objects.all()
    serializer_class = BenCampaignSerializer

class BenAdGroupViewSet(viewsets.ModelViewSet):
    #BenMetrics.objects.all().delete()
    queryset = BenAdGroup.objects.all()
    serializer_class = BenAdGroupSerializer

class BenMetricsViewSet(viewsets.ModelViewSet):
    #BenMetrics.objects.create(customer_resource_name= 'ben', campaign_id='23', ad_group_name='grp', metrics_cpc='1')
    #google_ads_client = GoogleAdsClient.load_from_storage("C:\\Users\\Shjon\\Documents\\codingprojects\\gittut\\secret\\google-ads.yaml")
    #djangoGAC(google_ads_client, "1255132966")
    #BenMetrics.objects.all().delete()
    queryset = BenMetrics.objects.all().order_by('datepulled')
    serializer_class = BenMetricsSerializer


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    #Hero.objects.all().delete() to delete all objects
    
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    #Hero.objects.update_or_create(name='Wonder Woman', alias='Diana', campaign_name='hello', campaign_id='1122')
   
    #google_ads_client = GoogleAdsClient.load_from_storage("C:\\Users\\Shjon\\Documents\\codingprojects\\gittut\\secret\\google-ads.yaml")
    #djangoGAC(google_ads_client, "1255132966")
    #createobject()
    
    #x = Hero.objects.create(name='bruce', alias='batman', campaign_name='mayor', campaign_id='190')
    #create has an autosave, dont need to next line x.save(), will get an error
    #Hero.objects.filter(id=207).update(name='brucewayne') this for updating
    #entry = Hero.objects.get(name='Wonder Woman')  for getting an obj error if multiple wonder womans
    
    #this is how to use updateorcreate, returns a tuple, one is retrieve obj, 
    #obj, created = Hero.objects.update_or_create(
    #name='Wonder Woman', campaign_id= 'nil',
    #defaults={'campaign_name':'testcampaign'},
    #)
    #print(obj, created)
    
    #print(entry.campaign_id) to print the object that we get
    #x = Hero.objects.latest('id', 'campaign_name') to get latest obj
    #x=Hero.objects.count() to count items in db
    #if queryset.filter(id=entry.id).exists(): 
        #print("Entry contained in queryset") to see if sth exist need to define entry as hero.objects.get...
    
@api_view( ['GET'] )
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'server is lvie current time is'
    return Response( data = message + date, status = status.HTTP_200_OK)


