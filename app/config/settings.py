"""
Configuration settings for the application.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    test_url: str = "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=UTC&date=today"
