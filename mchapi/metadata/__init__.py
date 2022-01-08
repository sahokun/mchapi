from mchapi import Define, APIBase
from mchapi.enum import LandEnum
from mchapi.util import datetime_fromtimestamp, timestamp_fromdatetime
from mchapi.metadata.models import HeroMetadata


class GetHeroMetadataAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_HERO_METADATA_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['hero_id']))

    def parse(self, response):
        name = response['name']
        description = response['description']
        image = response['image']

        attributes = response['attributes']
        type_name = attributes['type_name']
        lv = attributes['lv']
        rarity = attributes['rarity']
        hp = attributes['hp']
        phy = attributes['phy']
        int_ = attributes['int']
        agi = attributes['agi']
        active_skill = attributes['active_skill']
        passive_skill = attributes['passive_skill']

        external_url = response['external_url']
        image_url = response['image_url']
        home_url = response['home_url']

        extra_data = response['extra_data']
        active_skill_id = extra_data['active_skill_id']
        art_history = extra_data['art_history']
        ce = extra_data['ce']
        current_art = extra_data['current_art']
        current_stamina = extra_data['current_stamina']
        hero_type = extra_data['hero_type']
        max_stamina = extra_data['max_stamina']
        passive_skill_id = extra_data['passive_skill_id']

        timestamp = datetime_fromtimestamp(response['timestamp'])
        language = response['language']

        obj = HeroMetadata(name, description, image, type_name, lv, rarity, hp, phy, int_, agi, active_skill,
                           passive_skill, external_url, image_url, home_url, active_skill_id, art_history,
                           ce, current_art, current_stamina, hero_type, max_stamina, passive_skill_id,
                           timestamp, language)
        return obj


get_hero_metadata_api = GetHeroMetadataAPI()
