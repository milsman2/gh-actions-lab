"""
Testing settings.
"""
from pydantic import HttpUrl
from src.client import AioHttpClient
from src.config import app_settings


def test_settings():
    assert app_settings.TEST_URL == HttpUrl(
        "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=America/Chicago&date=today"
    )


def test_client():
    client = AioHttpClient()
    assert client is not None
