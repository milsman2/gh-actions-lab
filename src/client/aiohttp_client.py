"""
AIOHTTP Client module
"""
import aiohttp
from icecream import ic
from result import Err, Ok, Result
from typing import Optional


class AioHttpClient:
    """
    AIO Http Client class
    """

    def __init__(self) -> None:
        ic()
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        ic()
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        ic()
        if not self._session.closed:
            await self._session.close()

    async def get_data(self, url: str) -> Result[dict, str]:
        async with self._session as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return Err(f"Error fetching data. HTTP Status: {response.status}")
                return Ok(await response.json())
