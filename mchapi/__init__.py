from bs4 import BeautifulSoup
import requests
import json
import urllib.parse


__version__ = '0.0.1'


class Define:
    # METADATA API
    GET_HERO_METADATA_URL = "https://www.mycryptoheroes.net/metadata/hero/{0}"
    GET_HERO_TYPE_METADATA_URL = "https://www.mycryptoheroes.net/metadata/heroType/{0}"
    GET_EXTENSION_METADATA_URL = "https://www.mycryptoheroes.net/metadata/extension/{0}"
    GET_EXTENSION_TYPE_METADATA_URL = "https://www.mycryptoheroes.net/metadata/extensionType/{0}"
    GET_SKILL_METADATA_URL = "https://www.mycryptoheroes.net/metadata/skill/{0}"

    # ETH PROXY API
    GET_HERO_ASSET_URL = "https://www.mycryptoheroes.net/api/proxy/HeroAsset/heroes/{0}"
    GET_EXTENSION_ASSET_URL = "https://www.mycryptoheroes.net/api/proxy/ExtensionAsset/extensions/{0}"

    # MCH PROXY API
    GET_USER_INFO_URL = "https://www.mycryptoheroes.net/api/proxy/mch/users/{0}"
    GET_LAND_INFO_URL = "https://www.mycryptoheroes.net/api/proxy/mch/lands/{0}"
    GET_HERO_ASSET_INFO_URL = "https://www.mycryptoheroes.net/api/proxy/mch/heroes/{0}"
    GET_EXTENSION_ASSET_INFO_URL = "https://www.mycryptoheroes.net/api/proxy/mch/extensions/{0}"
    GET_HERO_SOLD_TRADES_URL = "https://www.mycryptoheroes.net/api/proxy/mch/trades/heroes/sold"
    GET_EXTENSION_SOLD_TRADES_URL = "https://www.mycryptoheroes.net/api/proxy/mch/trades/extensions/sold"


class APIBase:
    def parse(self, response):
        raise NotImplementedError()

    def get_url_with_params(self, **kwargs):
        raise NotImplementedError()

    def execute(self, **kwargs):
        url = self.get_url_with_params(**kwargs)
        r = requests.get(url)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('raise_for_status : {}'.format(e))
            if e.response.status_code == 404:
                return None
            raise e
        except Exception as e:
            print('raise_for_status : {}'.format(e))
            raise e

        soup = BeautifulSoup(r.content, "html.parser")
        response = json.loads(soup.string)
        return self.parse(response)

    @classmethod
    def make_query_dict(self, **kwargs):
        d = dict()
        for arg in kwargs:
            value = kwargs[arg]
            if value:
                d.update([(arg, value)])
        return d

    @classmethod
    def make_url(self, url, query_dict):
        query_string = urllib.parse.urlencode(query_dict)
        return url + (('?' + query_string) if query_string else '')
