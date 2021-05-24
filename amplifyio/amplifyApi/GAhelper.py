import argparse
import sys

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

def djangoGAC(client, customer_id):
    ga_service = client.get_service("GoogleAdsService", version="v6")

    query = """
        SELECT campaign.id, campaign.name
        FROM campaign
        ORDER BY campaign.id"""

    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id=customer_id , query=query)

    try:
        for batch in response:
            for row in batch.results:
                print(
                    f"{row.campaign.id}, {row.campaign.name}"
                    
                )

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