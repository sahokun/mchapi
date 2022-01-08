from mchapi import Define, APIBase
from mchapi.enum import LandEnum
from mchapi.util import datetime_fromtimestamp, timestamp_fromdatetime
from mchapi.eth.models import HeroAsset, ExtensionAsset


class GetHeroAssetAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_HERO_ASSET_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['address']))

    def parse(self, response):
        is_approved_for_all = response['is_approved_for_all']
        hero_ids = response['hero_ids']

        obj = HeroAsset(is_approved_for_all, hero_ids)
        return obj


class GetExtensionAssetAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_EXTENSION_ASSET_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['address']))

    def parse(self, response):
        is_approved_for_all = response['is_approved_for_all']
        extension_ids = response['extension_ids']

        obj = ExtensionAsset(is_approved_for_all, extension_ids)
        return obj


get_hero_asset_api = GetHeroAssetAPI()
get_extension_asset_api = GetExtensionAssetAPI()
