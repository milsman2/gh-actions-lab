"""
Configuration settings for the application.
"""

from pydantic_settings import BaseSettings
import os
from typing import Optional


class Settings(BaseSettings):
    TEST_URL: Optional[str] = os.getenv("TEST_URL")
