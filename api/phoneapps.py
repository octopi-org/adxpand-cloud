from api.ad_group_methods import create_ad_group, update_ad_group
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
import os
from django.contrib.auth.hashers import check_password
from google.ads.googleads import client
from .campaign_targetting_criteria import add_campaign_targeting_criteria
from .link_manage_to_cus import link_manager_to_client
from .models import Account, MyAccountManager, History
from .campaign_methods import update_campaign, add_campaign
from .keyword_methods import update_keywords, add_keywords, remove_keyword
from .GAfunctions import phone_login_GA_helper
from .ad_expanded_text_methods import add_expanded_text_ads, remove_expanded_text_ad, update_expanded_text_ad
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

# Please learn some Software Engineering Conventions. Helps a lot for your future Mods too. At the very least, no when to use snake_case, camelCase, PascalCase etc. Not too important for now.
# Also stuff like how to name variables covered in Software Convention also. Different Companies will use different styles. But in general, you work just a bit messy. 
# No worries though, these things take time to cultivate. Below are the ones provided by NUS. Can take a look (though i won't enforce it to be followed or anthing like that)
# GIT Conventions: https://se-education.org/guides/conventions/git.html
# Java Conventions(extendable to python): https://se-education.org/guides/conventions/java/intermediate.html
# Documentation Convention: https://developers.google.com/style (More for the future on how to write good documentation)
# Markdown Conventions (More for READMEs and using MD Language to generate documentation): https://se-education.org/guides/conventions/markdown.html
def phoneregisteraccount(account):
    #the app will post data to us,
    try:
        if account.method == 'POST':
            email1 = account.POST['email']
            password1 = account.POST['password']
            username1 = account.POST['username']

            #create new account on account models
            create_new_user_acc = Account.objects.create_user(
                email = email1, 
                username = username1,
                password = password1,    
                )
            create_new_user_acc.save()
            
            #check that new model is created
            newaccount = Account.objects.get(email1)
            print(newaccount)
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({"status": "failed"})

# to improve code reuse, you can abstract the block to it's own function and validate. Makes your life easier also.
# i.e. An "open lock" function and a "close lock" function
def phonelogin(info):
    try:
        if info.method == 'GET':
            email1 = info.GET['email']
            password1 = info.GET['password']
            #username1 = info.GET['username']
            
            try:
                #get account from accounts model
                grabexisting_acc = Account.objects.get( 
                    email = str(email1), 
                    
                    )
                
                #check pw same as one in account models
                check_pw = Account.objects.get(email = str(email1)).check_password(password1)
                if check_pw == True:
                    #calls phone_login_GA_helper from GAfunctions.py
                    ##################################################################################
                    # Include this block before calling Google Ads API DONT DELETE GOOD EG REFERENCE # 
                    ##################################################################################
                    data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
                    with open(json_key_file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    ####################################################

                    google_ads_client = GoogleAdsClient.load_from_dict(credentials)
                    new_dict = phone_login_GA_helper(google_ads_client ,"")

                    #######################################################
                    # Include this block after calling the Google Ads Api #
                    #######################################################
                    if os.path.exists(json_key_file_path):
                        print('KEYS has been deleted')
                        os.remove(json_key_file_path)
                    else:
                        print("KEYS don't exist")
                    #######################################################

                    return JsonResponse(new_dict)
            except:  
                return JsonResponse({'status':'failed'})   
    except:
        return JsonResponse({'status':'failed'})

# You can actually abstract out the info.POST object and use a seperate function to retrieve what you want. 
# Better still, you can just use the info.POST object directly as arguments in the relevant function params. 
def newcampaignbutton(info):
    try:
        if info.method == 'POST':
            campaign1 = str(info.POST['Campaign'])
            ad_grp_1 = str(info.POST['Ad Group'])
            #ad_name_1 = str(info.POST['Ad Name'])
            ad_title_1 = str(info.POST['Ad Title'])
            ad_describ_1 = str(info.POST['Ad Description'])
            keywords_1 = str(info.POST['Keywords'])
            budget_1 = str(info.POST['Budget'])
            location_1 = str(info.POST['Location'])
            
            ##################################################################################
            # Include this block before calling Google Ads API DONT DELETE GOOD EG REFERENCE # 
            ##################################################################################
            data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
            with open(json_key_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                ####################################################

            google_ads_client = GoogleAdsClient.load_from_dict(credentials)
            
            # Try to make code readable. Good practice. If you're going to multi line, multi line from the start
            return_campaign_id = add_campaign(client = google_ads_client, 
                customer_id = "7975644246", 
                choose_campaign_name=campaign1, 
                choose_budget_amt= budget_1 )
            
            return_ad_group_id = create_ad_group(client = google_ads_client, 
            customer_id= "", campaign_id= return_campaign_id, 
            choose_ad_grp_name = ad_grp_1)

            success_add_kw_dict = add_keywords(client = google_ads_client, customer_id = "", 
                ad_group_id = return_ad_group_id, 
                keyword_text = keywords_1)

            return_ad_id = add_expanded_text_ads(client = google_ads_client, customer_id = "", 
            ad_group_id = return_ad_group_id, number_of_ads = 1, update_ad_head_1 = ad_title_1, 
            update_ad_desc_1 = ad_describ_1)

            success_dict = { 'created campaign id' : return_campaign_id, 'created ad_group': return_ad_group_id,
            'added keywords': success_add_kw_dict, 'added ads' : return_ad_id }
            
            # Include this block after calling the Google Ads Api #
            if os.path.exists(json_key_file_path):
                print('KEYS has been deleted')
                os.remove(json_key_file_path)
            else:
                print("KEYS don't exist")
                    #######################################################
      
            #need to add to 3 models#_.objects.create()
            return JsonResponse(success_dict)
    except:
        return JsonResponse({'status':'failed'})


def editcampaignbutton(info):
    try:
        if info.method == 'POST':
            
            campaign_1 = str(info.POST['Campaign']) #this is campaign name
            ad_grp_1 = str(info.POST['Ad Group']) #is ad group name
            ad_title_1 = str(info.POST['Ad Title'])
            ad_describ_1 = str(info.POST['Ad Description'])
            kw_to_add_1 = str(info.POST['Keywords_To_Add']) #can do this but will run add_keywords method
            kw_to_del_1 = str(info.POST['Keywords_To_Del']) #cant do this 
            neg_kw_to_add_1 = str(info.POST['Negative_Keywords_To_Add']) 
            neg_kw_to_del_1 = str(info.POST['Negative_Keywords_To_Del'])
            budget_1 = str(info.POST['Budget'])
            location_1 = str(info.POST['Location'])
            
            data = json.loads(os.getenv("SECRET_KEY_04", SECRET_KEY_04))
            with open(json_key_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                ####################################################

            google_ads_client = GoogleAdsClient.load_from_dict(credentials)
            
            return_campaign_id = update_campaign(client = google_ads_client, customer_id = "", campaign_id = "",
                choose_campaign_name = campaign_1, choose_budget_amt= budget_1 )
            
            return_ad_group_id = update_ad_group(client = google_ads_client, 
            customer_id= "", ad_group_id = "", 
            cpc_bid_micro_amount = budget_1, edit_ad_grp_name = ad_grp_1)

#have to kiv this as keyword cant be deleted.  
            #success_add_kw_dict = update_keywords(client = google_ads_client, customer_id = "", 
                #ad_group_id = str_ad_group_id, 
                #keyword_text = keywords_1)

            return_ad_id = update_expanded_text_ad(client = google_ads_client, customer_id = "", 
            ad_group_id = return_ad_group_id, number_of_ads = 1, 
            update_ad_head_1 = ad_title_1, update_ad_desc_1 = ad_describ_1)

            return_op_success = add_campaign_targeting_criteria(client = google_ads_client, customer_id = "",
            campaign_id = return_campaign_id, keyword_text = neg_kw_to_add_1, location_id = location_1)

            success_dict = { 'updated campaign id' : return_campaign_id, 'updated ad_group': return_ad_group_id,
            'updated ad':return_ad_id, 'added negative keywords': return_op_success,}
            
            # Include this block after calling the Google Ads Api #
            if os.path.exists(json_key_file_path):
                print('KEYS has been deleted')
                os.remove(json_key_file_path)
            else:
                print("KEYS don't exist")
                    #######################################################

            #update into all 3 models #have yet to update the models
            #_.objects.update_or_create(
            #)
            return JsonResponse(success_dict)
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
            #above function works but i need to remodel the models first
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({'status':'failed'}) 
            