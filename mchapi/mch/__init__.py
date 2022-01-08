from mchapi import Define, APIBase
from mchapi.enum import LandEnum
from mchapi.util import datetime_fromtimestamp, timestamp_fromdatetime
from mchapi.mch.models import User, Land, HeroAsset, ExtensionAsset, HeroSoldTrades, ExtensionSoldTrades


class GetUserInfoAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_USER_INFO_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['user_id']))

    def parse(self, response):
        user_data = response['user_data']
        uid = user_data['uid']
        name = user_data['name'] if 'name' in user_data else ''
        land_type = user_data['land_type'] if 'land_type' in user_data else None
        land_since = user_data['land_since'] if 'land_since' in user_data else None
        class_type = user_data['class_type'] if 'class_type' in user_data else None
        prime_until = user_data['prime_until'] if 'prime_until' in user_data else None

        eth = user_data['eth'] if 'eth' in user_data else ''
        ema_levels_phy = 0
        ema_levels_int = 0
        ema_levels_heal = 0
        ema_levels_stamina = 0
        ema_levels_cut = 0
        ema_levels_charge = 0
        if 'ema_levels' in response['user_data']:
            ema_levels_phy = response['user_data']['ema_levels'][0]
            ema_levels_int = response['user_data']['ema_levels'][1]
            ema_levels_heal = response['user_data']['ema_levels'][2]
            ema_levels_stamina = response['user_data']['ema_levels'][3]
            ema_levels_cut = response['user_data']['ema_levels'][4]
            ema_levels_charge = response['user_data']['ema_levels'][5]

        eth = response['eth'] if 'eth' in response else ''
        # transfer_point = response['transfer_point'] if 'transfer_point' in response else None

        obj = User(uid, name, land_type, land_since, class_type, prime_until, ema_levels_phy,
                   ema_levels_int, ema_levels_heal, ema_levels_stamina, ema_levels_cut, ema_levels_charge, eth)
        # obj = User(uid, name, land_type, land_since, class_type, prime_until, eth, transfer_point)
        return obj


class GetLandInfoAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_LAND_INFO_URL

    def get_url_with_params(self, **kwargs):
        land_type = kwargs.get('land_type')
        if not land_type:
            land = kwargs.get('land')  # type: LandEnum
            land_type = land.value
        return self.__url__.format(str(land_type))

    def parse(self, response):
        name = response['name']
        citizens = response['citizens']

        obj = Land(name, citizens)
        return obj


class GetHeroAssetInfoAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_HERO_ASSET_INFO_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['user_id']))

    def parse(self, response):
        hero_ids = response['hero_ids']

        obj = HeroAsset(hero_ids)
        return obj


class GetExtensionAssetInfoAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_EXTENSION_ASSET_INFO_URL

    def get_url_with_params(self, **kwargs):
        return self.__url__.format(str(kwargs['user_id']))

    def parse(self, response):
        extension_ids = response['extension_ids']

        obj = ExtensionAsset(extension_ids)
        return obj


class GetHeroSoldTradesAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_HERO_SOLD_TRADES_URL

    def get_url_with_params(self, **kwargs):
        d = self.make_query_dict(since=timestamp_fromdatetime(kwargs.get(
            'since')), until=timestamp_fromdatetime(kwargs.get('until')))
        url = self.make_url(self.__url__, d)
        return url

    def parse(self, response):
        obj_list = list()
        for item in response:
            trade_id = item['trade_id']
            hero_id = item['hero_id']
            trade_since = item['trade_since']
            trade_until = item['trade_until']
            start_price = item['start_price']
            end_price = item['end_price']
            seller_id = item['seller_id']
            buyer_id = item['buyer_id']
            sold_at = item['sold_at']
            price = item['price']
            status = item['status']
            ce = item['ce']
            rarity = item['rarity']
            hp = item['hp']
            phy = item['phy']
            int_ = item['int']
            agi = item['agi']

            obj = HeroSoldTrades(trade_id, hero_id, trade_since, trade_until, start_price, end_price,
                                 seller_id, buyer_id, sold_at, price, status, ce, rarity, hp, phy, int_, agi)
            obj_list.append(obj)

        return obj_list


class GetExtensionSoldTradesAPI(APIBase):
    def __init__(self, define=Define):
        self.__url__ = define.GET_EXTENSION_SOLD_TRADES_URL

    def get_url_with_params(self, **kwargs):
        d = self.make_query_dict(since=timestamp_fromdatetime(kwargs.get(
            'since')), until=timestamp_fromdatetime(kwargs.get('until')))
        url = self.make_url(self.__url__, d)
        return url

    def parse(self, response):
        obj_list = list()
        for item in response:
            trade_id = item['trade_id']
            extension_id = item['extension_id']
            trade_since = item['trade_since']
            trade_until = item['trade_until']
            start_price = item['start_price']
            end_price = item['end_price']
            seller_id = item['seller_id']
            buyer_id = item['buyer_id']
            sold_at = item['sold_at']
            price = item['price']
            status = item['status']
            ce = item['ce']
            rarity = item['rarity']
            hp = item['hp']
            phy = item['phy']
            int_ = item['int']
            agi = item['agi']

            obj = HeroSoldTrades(trade_id, extension_id, trade_since, trade_until, start_price,
                                 end_price, seller_id, buyer_id, sold_at, price, status, ce, rarity, hp, phy, int_, agi)
            obj_list.append(obj)

        return obj_list


get_user_info_api = GetUserInfoAPI()
get_land_info_api = GetLandInfoAPI()
get_hero_asset_info_api = GetHeroAssetInfoAPI()
get_extension_asset_info_api = GetExtensionAssetInfoAPI()
get_hero_sold_trades_api = GetHeroSoldTradesAPI()
get_extension_sold_trades_api = GetExtensionSoldTradesAPI()
