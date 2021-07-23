from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import check_password
from .link_manage_to_cus import link_manager_to_client
from .models import Account, MyAccountManager, History
from .campaign_methods import update_campaign, add_campaign
from .keyword_methods import update_keywords, add_keywords
from .GAfunctions import phone_login_GA_helper



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
            print(create_new_user_acc)
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({"status": "failed"})


def phonelogin(info):
    try:
        if info.method == 'GET':
            email1 = info.GET['email']
            password1 = info.GET['password']
            username1 = info.GET['username']
            try:
                grabexisting_acc = Account.objects.get( 
                    email = str(email1), 
                    username = str(username1),
                    )
                
                check_pw = Account.objects.get(email = str(email1)).check_password(password1)
                
                #phone_login_GA_helper()
                return JsonResponse({'status':'success'})
            except:  
                return JsonResponse({'status':'acc not found'})   
    except:
        return str({'status':'failed'})


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
            History_Objects = History.objects.get('eeee')
            dict_of_hist_objs = json.dumps(History_Objects)
            #need GA method
            return JsonResponse(dict_of_hist_objs)
    except:
        return JsonResponse({'status':'failed'}) 

def connect_google_acc(info):
    try:
        if info.method == 'POST':
            cus_id = info.POST['Customer Id']
            link_manager_to_client(cus_id)
            return JsonResponse({'status':'linked'})
    except:
        return JsonResponse({'status':'failed'}) 
            