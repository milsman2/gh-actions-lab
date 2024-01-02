"""
Testing settings.
"""
from icecream import ic
from result import Err, Ok, Result

from src.client import AioHttpClient
from src.config import app_settings


def test_client():
    ic()
    client = AioHttpClient()
    assert client is not None


def test_settings():
    ic()
    assert app_settings.TEST_URL is not None
    assert app_settings.SUNRISE_SUNSET_URL is not None
    ic(app_settings.TEST_URL)
    ic(app_settings.SUNRISE_SUNSET_URL)


async def get_test_url() -> Result[dict, str]:
    ic()
    async with AioHttpClient() as http_client:
        ic()
        results = await http_client.get_data(str(app_settings.TEST_URL))
        match results:
            case Ok(data):
                ic(type(data))
                return Ok(data)
            case Err(err):
                ic(err)
                return Err(err)
