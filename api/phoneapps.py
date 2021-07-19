from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json

from .models import Account, MyAccountManager, 



'''
def phoneregisteraccount(account):
    #the app will post data to us,
    try:
        if account.method == 'POST':
            
            email1 = account.POST['email']
            password1 = account.POST['password']
            username1 = account.POST['username']
            accountmodel = get_user_model()
            create_newuser = accountmodel.objects.create_user(
                email = email1, 
                password = password1,    
                username = username1,
                )
            return JsonResponse({'status':'success'})
    except:
        return JsonResponse({"status": "failed"})
'''

def phonelogin(info):
    try:
        if info.method == 'GET':
            email1 = info.GET['email']
            #password1 = info.GET['password']
            username1 = info.GET['username']
            try:
                grabexisting_acc = Account.objects.get( 
                    email = str(email1), 
                    #password = str(password1), 
                    username = str(username1),
                    )
                
                return grabexisting_acc
            except:  
                return 'acc not found'   
    except:
        return str('failed')

'''
            if check == info:
                #insert method to get 12 pieces of info 
                #Clicks, CTR, CPC, Impressions, Search Impression Share, 
                # Search Exact Match Impression Share, Search Lost Impression Share (Rank), 
                # Search Lost Impression Share (Budget), Display Lost Impression Share (Rank), 
                # Display Lost Impression Share (Budget), Conversion Rate, Cost
                data = 'insert method here'
                response = json.dumps(data)
                #return data in dict form
            return JsonResponse(response)
          '''  
    


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
            #Ben_Tuition.objects.create()
            #needto create GA fn 
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
            keywords_1 = str(info.POST['Keywords'])
            budget_1 = str(info.POST['Budget'])
            location_1 = str(info.POST['Location'])
            #need to create GA fn
            #Ben_Tuition.objects.update_or_create(
            #)
            return JsonResponse({'campaign':'campaign edited'})
    except:
        return JsonResponse({'status':'failed'})
    
        
def kwrequestbutton(info):
    try:
        if info.method == 'GET':
            djangoGA_json()
        return JsonResponse({'kw':'kw requested'})

    except:
        return JsonResponse({'status':'failed'})



def get_change_history(info):
    try:
        if info.method == 'GET':
            History_Objects = History.objects.all()
            dict_of_hist_objs = json.dumps(History_Objects)
            #need GA method
            return JsonResponse(dict_of_hist_objs)
    except:
        return JsonResponse({'status':'failed'}) 

def connect_google_acc(info):
    try:
        if info.method == 'POST':
            info.POST['Customer Id']
            #link_manage_to_cus.py
            return JsonResponse({'status':'linked'})
    except:
        return JsonResponse({'status':'failed'}) 
            