import os
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import BenAdGroupSerializer, BenCampaignSerializer, BenMetricsSerializer
from .models import BenCampaign, BenAdGroup, BenMetrics
from .GAfunctions import djangoGA_json
from rest_framework.permissions import IsAuthenticated, AllowAny

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

# Google Ads API credentials masking
try:
    import cloud.settings._secrets as secure
    SECRET_KEY_02 = secure.SECRET_KEY_02
    SECRET_KEY_03 = secure.SECRET_KEY_03
    SECRET_KEY_04 = secure.SECRET_KEY_04
    SECRET_KEY_05 = secure.SECRET_KEY_05
except ImportError:
    SECRET_KEY_02 = "error_token"
    SECRET_KEY_03 = "error_token"
    SECRET_KEY_04 = "error_token"
    SECRET_KEY_05 = "error_token"

json_key_file_path = 'key.json'

credentials = {
    "developer_token": os.getenv("SECRET_KEY_02", SECRET_KEY_02),
    "login_customer_id": os.getenv("SECRET_KEY_03", SECRET_KEY_03),
    "json_key_file_path": json_key_file_path,
    "impersonated_email": os.getenv("SECRET_KEY_05", SECRET_KEY_05)
}

# Create your views here.

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
    ####################################################
    # Include this block before calling Google Ads API DONT DELETE GOOD EG REFERENCE # 
    ####################################################
    data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
    with open(json_key_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    ####################################################

    google_ads_client = GoogleAdsClient.load_from_dict(credentials)
    # djangoGAC(google_ads_client, "1255132966")
    BenMetrics.objects.all().delete()
    queryset = BenMetrics.objects.all().order_by('datepulled')
    serializer_class = BenMetricsSerializer
    
    #######################################################
    # Include this block after calling the Google Ads Api #
    #######################################################
    if os.path.exists(json_key_file_path):
        print('KEYS has been deleted')
        os.remove(json_key_file_path)
    else:
        print("KEYS don't exist")
    ###############################################################################


#this is for GA stuff
@api_view(['GET'])
#@permission_classes( [ AllowAny ] )
def GAlist(request):
    if request.method == 'GET':
        data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
        with open(json_key_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        google_ads_client = GoogleAdsClient.load_from_dict(credentials)
        GAjsonstr = djangoGA_json(google_ads_client, "1255132966")
        #GAjsonstr = 'test first'

        if os.path.exists(json_key_file_path):
            print('KEYS has been deleted')
            os.remove(json_key_file_path)
        else:
            print("KEYS don't exist")
    return Response(GAjsonstr)

'''
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
#