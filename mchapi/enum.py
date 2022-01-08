from enum import Enum


class EnumUtil:
    @classmethod
    def to_enum_or_blank(cls, enum, value):
        enum_value = enum.to_enum(value)
        return enum_value if enum_value is not None else ''


class LandEnum(Enum):
    """ランド"""
    Ocean = 1
    Strawberry = 2
    Tangerine = 3
    Lime = 4
    Graphite = 5
    Grape = 6
    Sage = 7
    Blueberry = 8
    Ruby = 9


class RarityEnum(Enum):
    """レアリティ"""
    Common = 1
    Uncommon = 2
    Rare = 3
    Epic = 4
    Legendary = 5
