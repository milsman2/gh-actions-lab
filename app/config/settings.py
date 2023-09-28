"""
Configuration settings for the application.
"""

from pydantic_settings import BaseSettings
from pydantic import HttpUrl


class Settings(BaseSettings):
    TEST_URL: HttpUrl = "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=UTC&date=today"
