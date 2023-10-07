"""
Testing settings.
"""
from src.config import settings
from pydantic import HttpUrl


def test_settings():
    assert settings.TEST_URL == HttpUrl(
        "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=America/Chicago&date=today"
    )
