from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import check_password
from google.ads.googleads import client
from .link_manage_to_cus import link_manager_to_client
from .models import Account, MyAccountManager, History
from .campaign_methods import update_campaign, add_campaign
from .keyword_methods import update_keywords, add_keywords
from .GAfunctions import phone_login_GA_helper
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

def phoneregisteraccount(account):
    #the app will post data to us,
    try:
        if account.method == 'POST':
            email1 = account.POST['email']
            password1 = account.POST['password']
            username1 = account.POST['username']

            create_new_user_acc = Account.objects.create_user(
                email = email1, 
                username = username1,
                password = password1,    
                )
            create_new_user_acc.save()
            #print(create_new_user_acc)
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({"status": "failed"})


def phonelogin(info):
    try:
        if info.method == 'GET':
            email1 = info.GET['email']
            password1 = info.GET['password']
            #username1 = info.GET['username']
            try:
                grabexisting_acc = Account.objects.get( 
                    email = str(email1), 
                    
                    )
                
                check_pw = Account.objects.get(email = str(email1)).check_password(password1)
                if check_pw == True:
                    google_ads_client = GoogleAdsClient.load_from_dict(credentials)
                    new_dict = phone_login_GA_helper(google_ads_client ,"1255132966")
                    return JsonResponse(new_dict)
            except:  
                return JsonResponse({'status':'failed'})   
    except:
        return JsonResponse({'status':'failed'})


def newcampaignbutton(info):
    try:
        if info.method == 'POST':
            campaign1 = str(info.POST['Campaign'])
            ad_grp_1 = str(info.POST['Ad Group'])
            ad_name_1 = str(info.POST['Ad Name'])
            ad_title_1 = str(info.POST['Ad Title'])
            ad_describ_1 = str(info.POST['Ad Description'])
            keywords_1 = str(info.POST['Keywords'])
            budget_1 = str(info.POST['Budget'])
            location_1 = str(info.POST['Location'])
            #add_campaign(client, customer_id)

            #need to add to 3 models
            #Ben_Tuition.objects.create()
            
            return JsonResponse({'campaign':'campaign created'})
    except:
        return JsonResponse({'status':'failed'})


def editcampaignbutton(info):
    try:
        if info.method == 'POST':
            
            campaign1 = str(info.POST['Campaign'])
            ad_grp_1 = str(info.POST['Ad Group'])
            ad_name_1 = str(info.POST['Ad Name'])
            ad_title_1 = str(info.POST['Ad Title'])
            ad_describ_1 = str(info.POST['Ad Description'])
            kw_to_add_1 = str(info.POST['Keywords_To_Add'])
            kw_to_del_1 = str(info.POST['Keywords_To_Del'])
            neg_kw_to_add_1 = str(info.POST['Negative_Keywords_To_Add'])
            neg_kw_to_del_1 = str(info.POST['Negative_Keywords_To_Del'])
            budget_1 = str(info.POST['Budget'])
            location_1 = str(info.POST['Location'])
            #update_campaign(client, customer_id, campaign_id)
            #update_keywords(client, customer_id, ad_group_id, criterion_id)
            
            #update into all 3 models
            #Ben_Tuition.objects.update_or_create(
            #)
            return JsonResponse({'campaign':'campaign edited'})
    except:
        return JsonResponse({'status':'failed'})
    
'''
def kwrequestbutton(info):
    try:
        if info.method == 'GET':
            djangoGA_json()
        return JsonResponse({'kw':'kw requested'})

    except:
        return JsonResponse({'status':'failed'})
'''


def get_change_history(info):
    try:
        if info.method == 'GET':
            History_Objects = History.objects.all()
            dict_of_hist_objs = json.dumps(History_Objects)
            
            return JsonResponse(dict_of_hist_objs)
    except:
        return JsonResponse({'status':'failed'}) 

def connect_google_acc(info):
    try:
        if info.method == 'POST':
            cus_id = info.POST['Customer Id']
            #return_str_manager_id = link_manager_to_client(customer_id= cus_id, manager_customer_id= '1__')
            #Account.objects.filter(str(username)).update(manager_id= return_str_manager_id)
            
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({'status':'failed'}) 
            