"""
Configuration settings for the application.
"""

from pydantic_settings import BaseSettings
from typing import Url


class Settings(BaseSettings):
    TEST_URL: Url = "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=UTC&date=today"
