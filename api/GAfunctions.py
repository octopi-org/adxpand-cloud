from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import sys
import json


#for database in drf puts data directly into database
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
                Ben_Metrics.objects.create( customer_resource_name = str(row.customer.resource_name), 
                campaign_name = str(row.campaign.name), campaign_id = str(row.campaign.id), 
                ad_group_name = str(row.ad_group.name), metrics_clicks = str(row.metrics.clicks),
                metrics_impressions = str(row.metrics.impressions), metrics_ctr = str(row.metrics.ctr),
                metrics_cpc = str(row.metrics.average_cpc), datepulled=str(row.segments.date))            

                #BenCampaign.objects.create(customer_resource_name = str(row.customer.resource_name), 
                

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




#for normal views converts to str json format
def djangoGA_json(client, customer_id):
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
        jsonlistobject = []
        for batch in response:
            for row in batch.results:  
                customer_resource_name = str(row.customer.resource_name) 
                campaign_name = str(row.campaign.name)
                campaign_id = str(row.campaign.id)
                ad_group_name = str(row.ad_group.name) 
                metrics_clicks = str(row.metrics.clicks)
                metrics_impressions = str(row.metrics.impressions)
                metrics_ctr = str(row.metrics.ctr)
                metrics_cpc = str(row.metrics.average_cpc) 
                datepulled = str(row.segments.date)  
                
                dictsample = {
                    'customername' : customer_resource_name,
                    'campaign_name' : campaign_name,
                    'campaign_id' : campaign_id,
                    'ad_group_name' : ad_group_name,
                    'metrics_clicks' : metrics_clicks,
                    'metrics_impressions' : metrics_impressions,
                    'metrics_ctr' : metrics_ctr,
                    'metrics_cpc' : metrics_cpc,
                    'datepulled' : datepulled
                }
                #strobject = "{"+"customername:{crn},"+"campaign_name:{cn},"+"campaign_id:{ci},"+"ad_group_name:{agn},"+"metrics_clicks:{mc},"+"metrics_impressions:{mi},"+"metrics_ctr:{mctr},"+"metrics_cpc:{mcpc},"+"datepulled:{dp}"+"}".format(crn = customer_resource_name, cn = campaign_name, ci = campaign_id, agn = ad_group_name, 
                #mc = metrics_clicks, mi = metrics_impressions, mctr = metrics_ctr, mcpc = metrics_cpc, dp = datepulled)
                jsonlistobject.append( dictsample )
        json_formatted_dict = { 
            'data':jsonlistobject
        }
        json_formatted_str = json.dumps(json_formatted_dict)
        return json_formatted_str

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



def phone_login_GA_helper(client, customer_id):
    ga_service = client.get_service("GoogleAdsService", version="v6")

    query = """
    SELECT metrics.search_impression_share, 
    metrics.search_exact_match_impression_share, 
    metrics.search_rank_lost_impression_share,  
    metrics.search_budget_lost_absolute_top_impression_share, 
    metrics.all_conversions_by_conversion_date, 
    metrics.average_cost, 
    customer.resource_name, 
    segments.date
    FROM ad_group 
    WHERE segments.date DURING LAST_30_DAYS """
#metrics.average_cost 
#metrics.all_conversions_by_conversion_date
    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id=customer_id , query=query)

    try:
        jsonlistobject = []
        for batch in response:
            for row in batch.results:  
                search_impres_share = str(row.metrics.search_impression_share)
                search_exact_match_impres_share = str(row.metrics.search_exact_match_impression_share) 
                search_rank_lost_impres_share = str(row.metrics.search_rank_lost_impression_share)
                search_budget_lost_abs_top_impres_share = str(row.metrics.search_budget_lost_absolute_top_impression_share) 
                all_conversions_by_conversion_date = str(row.metrics.all_conversions_from_interactions_rate) 
                metrics_average_cost = str(row.metrics.average_cost)
                customer_resource_name = str(row.customer.resource_name) 
                datepulled = str(row.segments.date)  

                dictsample = {
                    'search_impression_share' : search_impres_share,
                    'search_exact_match_impression_share' : search_exact_match_impres_share,
                    'search_rank_lost_impression_share' : search_rank_lost_impres_share,
                    'search_budget_lost_absolute_top_impression_share' : search_budget_lost_abs_top_impres_share,
                    'all_conversions_by_conversion_date' : all_conversions_by_conversion_date,
                    'metrics_average_cost' : metrics_average_cost, 
                    'customer_name' : customer_resource_name,  
                    'date_pulled' : datepulled,
                } 
                #strobject = "{"+"customername:{crn},"+"campaign_name:{cn},"+"campaign_id:{ci},"+"ad_group_name:{agn},"+"metrics_clicks:{mc},"+"metrics_impressions:{mi},"+"metrics_ctr:{mctr},"+"metrics_cpc:{mcpc},"+"datepulled:{dp}"+"}".format(crn = customer_resource_name, cn = campaign_name, ci = campaign_id, agn = ad_group_name, 
                #mc = metrics_clicks, mi = metrics_impressions, mctr = metrics_ctr, mcpc = metrics_cpc, dp = datepulled)
                jsonlistobject.append( dictsample )
        
        json_formatted_dict = { 
            'status':'success',
            'data':jsonlistobject,
        }
        #json_formatted_str = json.dumps(json_formatted_dict)
        return json_formatted_dict

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