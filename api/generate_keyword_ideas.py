import argparse
import sys, os
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

# Location IDs are listed here:
# https://developers.google.com/google-ads/api/reference/data/geotargets
# and they can also be retrieved using the GeoTargetConstantService as shown
# here: https://developers.google.com/google-ads/api/docs/targeting/location-targeting
#_DEFAULT_LOCATION_IDS = ["1023191"]  # location ID for New York, NY
_DEFAULT_LOCATION_IDS = ["2702"] #location ID for Singapore
# A language criterion ID. For example, specify 1000 for English. For more
# information on determining this value, see the below link:
# https://developers.google.com/google-ads/api/reference/data/codes-formats#expandable-7
_DEFAULT_LANGUAGE_ID = "1000"  # language ID for English


# [START generate_keyword_ideas]
def Gen_kw_ideas(
    client, customer_id, location_ids, language_id, keyword_texts
):
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")
    keyword_competition_level_enum = client.get_type(
        "KeywordPlanCompetitionLevelEnum"
    ).KeywordPlanCompetitionLevel
    keyword_plan_network = client.get_type(
        "KeywordPlanNetworkEnum"
    ).KeywordPlanNetwork.GOOGLE_SEARCH_AND_PARTNERS
    location_rns = _map_locations_ids_to_resource_names(client, location_ids)
    language_rn = client.get_service(
        "LanguageConstantService"
    ).language_constant_path(language_id)

    # Either keywords or a page_url are required to generate keyword ideas
    # so this raises an error if neither are provided.
    if not (keyword_texts):
        raise ValueError(
            "At least one of keywords or page URL is required, "
            "but neither was specified."
        )

    # Only one of the fields "url_seed", "keyword_seed", or
    # "keyword_and_url_seed" can be set on the request, depending on whether
    # keywords, a page_url or both were passed to this function.
    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = language_rn
    request.geo_target_constants = location_rns
    request.include_adult_keywords = False
    request.keyword_plan_network = keyword_plan_network

    # To generate keyword ideas with only a page_url and no keywords we need
    # to initialize a UrlSeed object with the page_url as the "url" field.
    #if not keyword_texts and page_url:
    #    request.url_seed.url = page_url

    # To generate keyword ideas with only a list of keywords and no page_url
    # we need to initialize a KeywordSeed object and set the "keywords" field
    # to be a list of StringValue objects.
    if keyword_texts:
        request.keyword_seed.keywords.extend(keyword_texts)

    # To generate keyword ideas using both a list of keywords and a page_url we
    # need to initialize a KeywordAndUrlSeed object, setting both the "url" and
    # "keywords" fields.
    #if keyword_texts and page_url:
    #    request.keyword_and_url_seed.url = page_url
    #    request.keyword_and_url_seed.keywords.extend(keyword_texts)

    keyword_ideas = keyword_plan_idea_service.generate_keyword_ideas(
        request=request
    )

    for idea in keyword_ideas:
        competition_value = idea.keyword_idea_metrics.competition.name
        print(
            f'Keyword idea text "{idea.text}" has '
            f'"{idea.keyword_idea_metrics.avg_monthly_searches}" '
            f'average monthly searches and "{competition_value}" '
            "competition.\n"
        )
    # [END generate_keyword_ideas]


def map_keywords_to_string_values(client, keyword_texts):
    keyword_protos = []
    for keyword in keyword_texts:
        string_val = client.get_type("StringValue")
        string_val.value = keyword
        keyword_protos.append(string_val)
    return keyword_protos


def _map_locations_ids_to_resource_names(client, location_ids):
    """Converts a list of location IDs to resource names.
    Args:
        client: an initialized GoogleAdsClient instance.
        location_ids: a list of location ID strings.
    Returns:
        a list of resource name strings using the given location IDs.
    """
    build_resource_name = client.get_service(
        "GeoTargetConstantService"
    ).geo_target_constant_path
    return [build_resource_name(location_id) for location_id in location_ids]

#my own function for button to insert keywords
def button_insert_keywords(keywords):
    listofkeywords = []
    listofkeywords.append(keywords)
    Gen_kw_ideas( 
        client = GoogleAdsClient.load_from_dict(credentials),
        customer_id = "1_",
        location_ids=["2702"],
        language_id="1000",
        keyword_texts=listofkeywords)


