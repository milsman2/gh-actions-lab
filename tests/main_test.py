"""
Testing settings.
"""
from src.client import AioHttpClient


def test_client():
    client = AioHttpClient()
    assert client is not None
