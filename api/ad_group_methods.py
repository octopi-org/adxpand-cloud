#!/usr/bin/env python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example updates an ad group.
To get ad groups, run get_ad_groups.py.
"""

import argparse
import sys
import uuid

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.api_core import protobuf_helpers

_DEFAULT_PAGE_SIZE = 1000


def create_ad_group(client, customer_id, campaign_id, choose_ad_grp_name):
    #my added fields
    final_ad_grp_name = choose_ad_grp_name
    
    
    ad_group_service = client.get_service("AdGroupService")
    campaign_service = client.get_service("CampaignService")

    # Create ad group.
    ad_group_operation = client.get_type("AdGroupOperation")
    ad_group = ad_group_operation.create
    ad_group.name = f"{final_ad_grp_name}, {uuid.uuid4()}"
    ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
    ad_group.campaign = campaign_service.campaign_path(customer_id, campaign_id)
    ad_group.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    ad_group.cpc_bid_micros = 10000000 

    # Add the ad group.
    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=customer_id, operations=[ad_group_operation]
    )
    print(f"Created ad group {ad_group_response.results[0].resource_name}.")
    return(str(ad_group.id))

#add ad grp
'''parser.add_argument( "-c", "--customer_id", type=str, required=True, help="The Google Ads customer ID.", )
parser.add_argument("-i", "--campaign_id", type=str, required=True, help="The campaign ID." )'''


# [START update_ad_group]
def update_ad_group(client, customer_id, ad_group_id, cpc_bid_micro_amount, edit_ad_grp_name):
    final_ad_grp_name = str(edit_ad_grp_name)

    ad_group_service = client.get_service("AdGroupService")

    # Create ad group operation.
    ad_group_operation = client.get_type("AdGroupOperation")
    ad_group = ad_group_operation.update
    ad_group.name = final_ad_grp_name #added line #works
    ad_group.resource_name = ad_group_service.ad_group_path(
        customer_id, ad_group_id
    )
    ad_group.status = client.enums.AdGroupStatusEnum.PAUSED
    ad_group.cpc_bid_micros = cpc_bid_micro_amount
    client.copy_from(
        ad_group_operation.update_mask,
        protobuf_helpers.field_mask(None, ad_group._pb),
    )

    # Update the ad group.
    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=customer_id, operations=[ad_group_operation]
    )

    print(f"Updated ad group {ad_group_response.results[0].resource_name}.")
    return {'status': ad_group_response.results[0].resource_name}
    # [END update_ad_group]


#how to update
'''
    parser.add_argument("-c","--customer_id", type=str, required=True, help="The Google Ads customer ID.",)
    parser.add_argument("-a", "--ad_group_id", type=str, required=True, help="The ad group ID.")
    parser.add_argument( "-b", "--cpc_bid_micro_amount", type=int, required=True, help="The cpc bid micro amount.")   '''

def get_ad_group(client, customer_id, page_size, campaign_id=None):
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          campaign.id,
          ad_group.id,
          ad_group.name
        FROM ad_group"""

    if campaign_id:
        query += f" WHERE campaign.id = {campaign_id}"

    search_request = client.get_type("SearchGoogleAdsRequest")
    search_request.customer_id = customer_id
    search_request.query = query
    search_request.page_size = _DEFAULT_PAGE_SIZE

    results = ga_service.search(request=search_request)

    for row in results:
        print(
            f"Ad group with ID {row.ad_group.id} and name "
            f'"{row.ad_group.name}" was found in campaign with '
            f"ID {row.campaign.id}."
        )

'''
    parser = argparse.ArgumentParser( description="List ad groups for specified customer.")
    parser.add_argument("-c","--customer_id",type=str,required=True,help="The Google Ads customer ID.".)
    parser.add_argument("-i","--campaign_id",type=str,required=False,help=("The campaign ID. Specify this to list ad groups " "solely for this campaign ID."),)'''