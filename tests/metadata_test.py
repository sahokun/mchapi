import unittest
from mchapi.metadata import get_hero_metadata_api
from mchapi.metadata.models import HeroMetadata


class HeroMetadataAPITest(unittest.TestCase):
    def test_execute(self):
        obj = get_hero_metadata_api.execute(hero_id=40420035)  # type: HeroMetadata

        self.assertEqual(obj.attributes.type_name, 'Buddha')
        print(obj.attributes.type_name)
