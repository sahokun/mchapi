import unittest
from mchapi.eth import get_hero_asset_api, get_extension_asset_api


class HeroAssetAPITest(unittest.TestCase):
    def test_execute(self):
        obj = get_hero_asset_api.execute(address='0x4752D96A0564728c596ae067844c2d1EDFf37131')

        self.assertTrue(isinstance(obj.hero_ids, list))
        print(obj.hero_ids)


class ExtensionAssetAPITest(unittest.TestCase):
    def test_execute(self):
        obj = get_extension_asset_api.execute(address='0x4752D96A0564728c596ae067844c2d1EDFf37131')

        self.assertTrue(isinstance(obj.extension_ids, list))
        print(obj.extension_ids)
