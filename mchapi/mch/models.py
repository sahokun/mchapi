from mchapi.util import enum_value_to_name, datetime_fromtimestamp
from mchapi.enum import LandEnum, RarityEnum


class User:
    def __init__(self, uid, name, land_type, land_since, class_type, prime_until, ema_levels_phy, ema_levels_int, ema_levels_heal, ema_levels_stamina, ema_levels_cut, ema_levels_charge, eth):
        self.uid = uid
        self.name = name
        self.land_type = enum_value_to_name(LandEnum, land_type)
        self.land_since = datetime_fromtimestamp(land_since)
        self.class_type = class_type
        self.prime_until = datetime_fromtimestamp(prime_until)
        self.eth = eth
        self.ema_levels_phy = ema_levels_phy
        self.ema_levels_int = ema_levels_int
        self.ema_levels_heal = ema_levels_heal
        self.ema_levels_stamina = ema_levels_stamina
        self.ema_levels_cut = ema_levels_cut
        self.ema_levels_charge = ema_levels_charge
        # self.ema_rate1000s = self.get_ema_rate1000s()
        self.eth = eth
        # self.transfer_point = transfer_point


class Land:
    def __init__(self, name, citizens):
        self.name = name
        self.citizens = citizens


class HeroAsset:
    def __init__(self, hero_ids):
        self.hero_ids = hero_ids


class ExtensionAsset:
    def __init__(self, extension_ids):
        self.extension_ids = extension_ids


class SoldTrades:
    def __init__(self, trade_id, trade_since, trade_until, start_price, end_price, seller_id, buyer_id, sold_at, price, status, ce, rarity, hp, phy, int_, agi):
        self.trade_id = trade_id
        self.trade_since = datetime_fromtimestamp(trade_since)
        self.trade_until = datetime_fromtimestamp(trade_until)
        self.start_price = start_price
        self.end_price = end_price
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.sold_at = datetime_fromtimestamp(sold_at)
        self.price = price
        self.status = status
        self.ce = ce
        self.rarity = enum_value_to_name(RarityEnum, rarity)
        self.hp = hp
        self.phy = phy
        self.int_ = int_
        self.agi = agi


class HeroSoldTrades(SoldTrades):
    def __init__(self, trade_id, hero_id, trade_since, trade_until, start_price, end_price, seller_id, buyer_id, sold_at, price, status, ce, rarity, hp, phy, int_, agi):
        super().__init__(trade_id, trade_since, trade_until, start_price, end_price, seller_id, buyer_id, sold_at, price, status, ce , rarity, hp, phy, int_, agi)
        self.hero_id = hero_id


class ExtensionSoldTrades(SoldTrades):
    def __init__(self, trade_id, extension_id, trade_since, trade_until, start_price, end_price, seller_id, buyer_id, sold_at, price, status, ce, rarity, hp, phy, int_, agi):
        super().__init__(trade_id, trade_since, trade_until, start_price, end_price, seller_id, buyer_id, sold_at, price, status, ce , rarity, hp, phy, int_, agi)
        self.extension_id = extension_id
