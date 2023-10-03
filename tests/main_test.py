"""
Testing settings.
"""
from src.config.settings import Settings
from pydantic import HttpUrl


def test_settings():
    settings = Settings()
    assert settings.TEST_URL == HttpUrl(
        "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=America/Chicago&date=today"
    )
