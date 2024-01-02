"""
Configuration settings for the application.
"""

import os
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TEST_URL: Optional[str] = os.getenv(
        "TEST_URL",
        "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=America/Chicago&date=today",
    )
    SUNRISE_SUNSET_URL: Optional[str] = os.getenv("SUNRISE_SUNSET_URL", None)
