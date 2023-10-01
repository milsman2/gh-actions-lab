"""
Configuration settings for the application.
"""

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TEST_URL: HttpUrl = "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=America/Chicago&date=today"
