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
"""This example adds an expanded text ad.
To get expanded text ads, run get_expanded_text_ads.py.
"""


import argparse
import sys
import uuid

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.api_core import protobuf_helpers



# [START add_expanded_text_ads]
def add_expanded_text_ads(client, customer_id, ad_group_id, number_of_ads,
    **data):

    try:
        if 'update_ad_head_1' in data:
            ad_headline_1 = str(data['update_ad_head_1'])

        if 'update_ad_head_2' in data:
            ad_headline_2 = str(data['update_ad_head_2'])

        if 'update_ad_head_3' in data:
            ad_headline_3 = str(data['update_ad_head_3'])

        if 'update_ad_desc_1' in data:
            ad_desc_1 = str(data['update_ad_desc_1'])

        if 'update_ad_desc_2' in data:
            ad_desc_2 = str(data['update_ad_desc_2'])

        if data == {}:
            print('cant be empty')
    except:
        print('error')

    ad_group_ad_service = client.get_service("AdGroupAdService")
    ad_group_service = client.get_service("AdGroupService")

    ad_group_ad_operations = []
    for i in range(number_of_ads):
        # Create ad group ad.
        ad_group_ad_operation = client.get_type("AdGroupAdOperation")
        ad_group_ad = ad_group_ad_operation.create
        ad_group_ad.ad_group = ad_group_service.ad_group_path(
            customer_id, ad_group_id
        )
        ad_group_ad.status = client.enums.AdGroupAdStatusEnum.PAUSED

        # Set expanded text ad info
        ad_group_ad.ad.final_urls.append("http://www.example.com")
        
        if 'update_ad_desc_1' in data:
            ad_desc_1 = str(data['update_ad_desc_1'])

            ad_group_ad.ad.expanded_text_ad.description = f"{ad_desc_1}"

        if 'update_ad_head_1' in data:
            ad_headline_1 = str(data['update_ad_head_1'])

            ad_group_ad.ad.expanded_text_ad.headline_part1 = (
                f"{ad_headline_1} {i} {str(uuid.uuid4())[:8]}"
            )
        
        if 'update_ad_head_2' in data:
            ad_headline_2 = str(data['update_ad_head_2'])

            ad_group_ad.ad.expanded_text_ad.headline_part2 = (
                f"{ad_headline_2}"
            )
        ad_group_ad.ad.expanded_text_ad.path1 = "all-inclusive"
        ad_group_ad.ad.expanded_text_ad.path2 = "deals"

        ad_group_ad_operations.append(ad_group_ad_operation)

    ad_group_ad_response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=customer_id, operations=ad_group_ad_operations
    )

    for result in ad_group_ad_response.results:
        print(f'Created ad group ad "{result.resource_name}".')
        str_ad_grp_id = f'Created ad group ad "{result.resource_name}".'
    return str_ad_grp_id
    # [END add_expanded_text_ads]

'''
        description=(
"Adds an expanded text ad to the specified ad group ID, ""for the given customer ID."))
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c","--customer_id", type=str,required=True,help="The Google Ads customer ID.",)
    parser.add_argument("-a", "--ad_group_id", type=str, required=True, help="The ad group ID." )
    parser.add_argument("-n","--number_of_ads", type=int, required=False, default=1,
        help="The number of ads.",)'''

#get expanded text ad
def get_expanded_text_ad(client, customer_id, ad_group_id=None):
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          ad_group.id,
          ad_group_ad.ad.id,
          ad_group_ad.ad.expanded_text_ad.headline_part1,
          ad_group_ad.ad.expanded_text_ad.headline_part2,
          ad_group_ad.status
        FROM ad_group_ad
        WHERE ad_group_ad.ad.type = EXPANDED_TEXT_AD"""

    if ad_group_id:
        query += f" AND ad_group.id = {ad_group_id}"

    response = ga_service.search_stream(customer_id=customer_id, query=query)

    for batch in response:
        for row in batch.results:
            ad = row.ad_group_ad.ad

            if ad.expanded_text_ad:
                expanded_text_ad_info = ad.expanded_text_ad

            print(
                f"Expanded text ad with ID {ad.id}, status "
                f'"{row.ad_group_ad.status.name}", and headline '
                f'"{expanded_text_ad_info.headline_part1}" - '
                f'"{expanded_text_ad_info.headline_part2}" was '
                f"found in ad group with ID {row.ad_group.id}."
            )

'''
    parser.add_argument("-c","--customer_id",type=str,required=True,help="The Google Ads customer ID.",)
    parser.add_argument("-a","--ad_group_id",type=str,required=False,help="The ad group ID. ",)
    '''


'''ad_headline_1, ad_headline_2, 
    ad_headline_3, ad_desc_1, ad_desc_2):
    update_ad_head_1 = str(ad_headline_1)
    update_ad_head_2 = str(ad_headline_2)
    update_ad_head_3 = str(ad_headline_3)
    update_ad_desc_1 = str(ad_desc_1)
    update_ad_desc_2 = str(ad_desc_2)'''


#update expanded text ad
def update_expanded_text_ad(client, customer_id, ad_id ):
    

    ad_service = client.get_service("AdService")
    ad_operation = client.get_type("AdOperation")

    # Update ad operation.
    ad = ad_operation.update
    ad.resource_name = ad_service.ad_path(customer_id, ad_id)
    ad.expanded_text_ad.headline_part1 = (
        f"Cruise to Pluto {str(uuid.uuid4())[:8]}"
    )
    ad.expanded_text_ad.headline_part2 = "Tickets on sale now"
    ad.expanded_text_ad.description = "Best space cruise ever."
    ad.final_urls.append("http://www.example.com")
    ad.final_mobile_urls.append("http://www.example.com/mobile")
    client.copy_from(
        ad_operation.update_mask, protobuf_helpers.field_mask(None, ad._pb)
    )

    # Updates the ad.
    ad_response = ad_service.mutate_ads(
        customer_id=customer_id, operations=[ad_operation]
    )
    print(
        f'Ad with resource name "{ad_response.results[0].resource_name}" '
        "was updated."
    )
    # [END update_expanded_text_ad]

'''
    # The following argument(s) should be provided to run the example.
    parser.add_argument("-c","--customer_id",type=str,required=True,help="The Google Ads customer ID.",)
    parser.add_argument("-i", "--ad_id", type=str, required=True, help="The ad ID.")'''



#remove expanded text ad
def remove_expanded_text_ad(client, customer_id, ad_group_id, ad_id):
    ad_group_ad_service = client.get_service("AdGroupAdService")
    ad_group_ad_operation = client.get_type("AdGroupAdOperation")

    resource_name = ad_group_ad_service.ad_group_ad_path(
        customer_id, ad_group_id, ad_id
    )
    ad_group_ad_operation.remove = resource_name

    ad_group_ad_response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=customer_id, operations=[ad_group_ad_operation]
    )

    print(
        f"Removed ad group ad {ad_group_ad_response.results[0].resource_name}."
    )

'''
    parser.add_argument("-c","--customer_id",type=str,required=True,help="The Google Ads customer ID.",)
    parser.add_argument("-a", "--ad_group_id", type=str, required=True, help="The ad group ID.")
    parser.add_argument("-i", "--ad_id", type=str, required=True, help="The ad ID.")'''