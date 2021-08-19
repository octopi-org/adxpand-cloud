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
"""This example updates a keyword for the specified ad group."""


import argparse
import sys

from google.api_core import protobuf_helpers
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def add_keywords(client, customer_id, ad_group_id, keyword_text):
    ad_group_service = client.get_service("AdGroupService")
    ad_group_criterion_service = client.get_service("AdGroupCriterionService")

    # Create keyword.
    ad_group_criterion_operation = client.get_type("AdGroupCriterionOperation")
    ad_group_criterion = ad_group_criterion_operation.create
    ad_group_criterion.ad_group = ad_group_service.ad_group_path(
        customer_id, ad_group_id
    )
    ad_group_criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
    ad_group_criterion.keyword.text = keyword_text
    ad_group_criterion.keyword.match_type = (
        client.enums.KeywordMatchTypeEnum.EXACT
    )

    # Optional field
    # All fields can be referenced from the protos directly.
    # The protos are located in subdirectories under:
    # https://github.com/googleapis/googleapis/tree/master/google/ads/googleads
    # ad_group_criterion.negative = True

    # Optional repeated field
    # ad_group_criterion.final_urls.append('https://www.example.com')

    # Add keyword
    ad_group_criterion_response = (
        ad_group_criterion_service.mutate_ad_group_criteria(
            customer_id=customer_id,
            operations=[ad_group_criterion_operation],
        )
    )

    print(
        "Created keyword "
        f"{ad_group_criterion_response.results[0].resource_name}."
    )
    return({'status':'success'})


def update_keywords(client, customer_id, ad_group_id, criterion_id):
    agc_service = client.get_service("AdGroupCriterionService")
    ad_group_criterion_operation = client.get_type("AdGroupCriterionOperation")

    ad_group_criterion = ad_group_criterion_operation.update
    ad_group_criterion.resource_name = agc_service.ad_group_criterion_path(
        customer_id, ad_group_id, criterion_id
    )
    ad_group_criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
    ad_group_criterion.final_urls.append("https://www.example.com")
    client.copy_from(
        ad_group_criterion_operation.update_mask,
        protobuf_helpers.field_mask(None, ad_group_criterion._pb),
    )

    agc_response = agc_service.mutate_ad_group_criteria(
        customer_id=customer_id, operations=[ad_group_criterion_operation]
    )
    print(f"Updated keyword {agc_response.results[0].resource_name}.")

'''
    parser.add_argument(
        "-c", "--customer_id", type=str,
        required=True, help="The Google Ads customer ID.",)
    parser.add_argument(
        "-a", "--ad_group_id", type=str, required=True, help="The ad group ID.")
    parser.add_argument(
        "-k",  "--criterion_id", type=str, required=True,  help="The criterion ID, or keyword ID.",)'''


def remove_keyword(client, customer_id, ad_group_id, criterion_id):
    agc_service = client.get_service("AdGroupCriterionService")
    agc_operation = client.get_type("AdGroupCriterionOperation")

    resource_name = agc_service.ad_group_criterion_path(
        customer_id, ad_group_id, criterion_id
    )
    agc_operation.remove = resource_name

    agc_response = agc_service.mutate_ad_group_criteria(
        customer_id=customer_id, operations=[agc_operation]
    )

    print(f"Removed keyword {agc_response.results[0].resource_name}.")
