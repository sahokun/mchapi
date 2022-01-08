import unittest
from mchapi.mch import get_user_info_api, get_land_info_api, get_hero_asset_info_api, get_extension_asset_info_api, get_hero_sold_trades_api, get_extension_sold_trades_api
from mchapi.enum import LandEnum
from datetime import datetime


class UserInfoTest(unittest.TestCase):
    def test_execute(self):
        obj = get_user_info_api.execute(user_id='18793')

        self.assertEqual(18793, obj.uid)
        print(str(obj.uid) + ': ' + obj.name)
        print(obj.land_type + ': ' + str(obj.land_since))


class LandInfoTest(unittest.TestCase):
    def test_land_type_execute(self):
        obj = get_land_info_api.execute(land_type=1)

        self.assertEqual('Ocean', obj.name)
        print(obj.name + ': ' + str(obj.citizens))

    def test_land_execute(self):
        obj = get_land_info_api.execute(land=LandEnum.Ocean)

        self.assertEqual('Ocean', obj.name)
        print(obj.name + ': ' + str(obj.citizens))


class HeroAssetInfoTest(unittest.TestCase):
    def test_execute(self):
        obj = get_hero_asset_info_api.execute(user_id='18793')

        expected = 50280011
        self.assertTrue(expected in obj.hero_ids)
        print(obj.hero_ids)

    def test_error_execute(self):
        obj = get_hero_asset_info_api.execute(user_id='')

        expected = None
        self.assertEqual(expected, obj)


class ExtensionAssetInfoTest(unittest.TestCase):
    def test_execute(self):
        obj = get_extension_asset_info_api.execute(user_id='10001')
        print(obj.extension_ids)

        expected = 10011273
        self.assertTrue(expected in obj.extension_ids)

    def test_error_execute(self):
        obj = get_extension_asset_info_api.execute(user_id='')

        expected = None
        self.assertEqual(expected, obj)


class HeroSoldTradesTest(unittest.TestCase):
    def test_execute(self):
        obj_list = get_hero_sold_trades_api.execute()

        self.assertTrue(isinstance(obj_list, list))
        print(obj_list)

    def test_param_execute(self):
        obj_list = get_hero_sold_trades_api.execute(since=datetime(
            2020, 1, 9, 19, 28, 57, 0), until=datetime(2020, 1, 10, 19, 28, 57, 0))
        self.assertTrue(isinstance(obj_list, list))
        response_list = list()
        response_list.append(
            ','.join(['price', 'buyer_id', 'seller_id', 'sold_at', 'status', 'ce']))
        for item in obj_list:
            output_list = [str(item.price), str(item.buyer_id), str(item.seller_id), str(
                "{0:%Y-%m-%d}".format(item.sold_at)), item.status, str(item.ce)]
            response_list.append(','.join(output_list))

        print(response_list)


class ExtensionSoldTradesTest(unittest.TestCase):
    def test_execute(self):
        obj_list = get_extension_sold_trades_api.execute()

        self.assertTrue(isinstance(obj_list, list))
        print(obj_list)

    def test_param_execute(self):
        obj_list = get_extension_sold_trades_api.execute(since=datetime(
            2020, 1, 9, 19, 28, 57, 0), until=datetime(2020, 1, 10, 19, 28, 57, 0))

        self.assertTrue(isinstance(obj_list, list))
        print(obj_list)
