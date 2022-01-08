from mchapi.util import enum_value_to_name, datetime_fromtimestamp


class HeroMetadata:
    class Attributes:
        def __init__(self, type_name, lv, rarity, hp, phy, int_, agi, active_skill, passive_skill):
            self.type_name = type_name
            self.lv = lv
            self.rarity = rarity
            self.hp = hp
            self.phy = phy
            self.int_ = int_
            self.agi = agi
            self.active_skill = active_skill
            self.passive_skill = passive_skill

    class ExtraData:
        def __init__(self, active_skill_id, art_history, ce, current_art, current_stamina, hero_type,
                     max_stamina, passive_skill_id):
            self.active_skill_id = active_skill_id
            self.art_history = art_history
            self.ce = ce
            self.current_art = current_art
            self.current_stamina = current_stamina
            self.hero_type = hero_type
            self.max_stamina = max_stamina
            self.passive_skill_id = passive_skill_id

    def __init__(self, name, description, image, type_name, lv, rarity, hp, phy, int_, agi, active_skill,
                 passive_skill, external_url, image_url, home_url, active_skill_id, art_history, ce,
                 current_art, current_stamina, hero_type, max_stamina, passive_skill_id, timestamp, language):
        self.name = name
        self.description = description
        self.image = image
        attributes = self.Attributes(type_name, lv, rarity, hp, phy, int_, agi, active_skill, passive_skill)
        self.attributes = attributes
        self.external_url = external_url
        self.image_url = image_url
        self.home_url = home_url
        extra_data = self.ExtraData(active_skill_id, art_history, ce, current_art, current_stamina, hero_type, max_stamina, passive_skill_id)
        self.extra_data = extra_data
        self.timestamp = timestamp
        self.language = language


class HeroTypeMetadata:
    class Name:
        def __init__(self, en, ja, zh):
            self.en = en
            self.ja = ja
            self.zh = zh

    # class ExtraData:
    #     def __init__(self, active_skill_id, art_history, ce, current_art, current_stamina, hero_type,
    #                  max_stamina, passive_skill_id):
    #         self.active_skill_id = active_skill_id
    #         self.art_history = art_history
    #         self.ce = ce
    #         self.current_art = current_art
    #         self.current_stamina = current_stamina
    #         self.hero_type = hero_type
    #         self.max_stamina = max_stamina
    #         self.passive_skill_id = passive_skill_id

    # def __init__(self, name, description, image, type_name, lv, rarity, hp, phy, int_, agi, active_skill,
    #              passive_skill, external_url, image_url, home_url, active_skill_id, art_history, ce,
    #              current_art, current_stamina, hero_type, max_stamina, passive_skill_id, timestamp, language):
    #     self.name = name
    #     self.description = description
    #     self.image = image
    #     attributes = self.Attributes(type_name, lv, rarity, hp, phy, int_, agi, active_skill, passive_skill)
    #     self.attributes = attributes
    #     self.external_url = external_url
    #     self.image_url = image_url
    #     self.home_url = home_url
    #     extra_data = self.ExtraData(active_skill_id, art_history, ce, current_art, current_stamina, hero_type, max_stamina, passive_skill_id)
    #     self.extra_data = extra_data
    #     self.timestamp = timestamp
    #     self.language = language
