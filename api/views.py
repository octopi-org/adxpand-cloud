import os
import json
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import BenAdGroupSerializer, BenCampaignSerializer, BenMetricsSerializer
from .models import BenCampaign, BenAdGroup, BenMetrics, MyAccountManager, Account
from .GAfunctions import djangoGA_json
from .generate_keyword_ideas import Gen_kw_ideas, map_keywords_to_string_values, _map_locations_ids_to_resource_names
from .add_keyword_plan import GA_add_kw_plan
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from django.views import View
from .phoneapps import phonelogin

from django.contrib.auth import get_user_model


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
@permission_classes( [ AllowAny ] )
def GAlist(request):
    if request.method == 'GET':
        data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
        with open(json_key_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        google_ads_client = GoogleAdsClient.load_from_dict(credentials)
        #GAjsonstr = djangoGA_json(google_ads_client, "1255132966")
        GAjsonstr = 'test first'

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

@api_view( ['GET'] )
@permission_classes( [AllowAny])
def index(request):
    if request.method == 'GET':
        data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
        with open(json_key_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        #googleads_client = GoogleAdsClient.load_from_dict(credentials)
        data1 = GA_add_kw_plan(
            client=GoogleAdsClient.load_from_dict(credentials),
            customer_id="1255132966" )
        

        if os.path.exists(json_key_file_path):
            print('KEYS has been deleted')
            os.remove(json_key_file_path)
        else:
            print("KEYS don't exist")

    return Response( data1)

'''
@permission_classes([AllowAny])
class AppGetView(View):
    info='test'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.info ,status=status.HTTP_200_OK)
'''
'''
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        # Actually record interest somehow here!

        return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))
        '''

@permission_classes([AllowAny])
class AppGetView(View):
    
    def get(self, request, *args, **kwargs):
        informa = phonelogin(request)
        print(informa)
        return HttpResponse(informa ,status=status.HTTP_200_OK)