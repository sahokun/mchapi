from mchapi.util import enum_value_to_name, datetime_fromtimestamp


class HeroAsset:
    def __init__(self, is_approved_for_all, hero_ids):
        self.is_approved_for_all = is_approved_for_all
        self.hero_ids = hero_ids


class ExtensionAsset:
    def __init__(self, is_approved_for_all, extension_ids):
        self.is_approved_for_all = is_approved_for_all
        self.extension_ids = extension_ids
