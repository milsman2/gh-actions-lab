"""
AIOHTTP Client module
"""
from typing import Optional

import aiohttp
from icecream import ic
from result import Err, Ok, Result


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
        ic(self._session)
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        ic()
        if self._session is not None:
            if self._session.closed is False:
                await self._session.close()
            ic(self._session.closed)

    async def get_data(self, url: str) -> Result[dict, str]:
        ic()
        if self._session is None:
            return Err("Session not initialized.")
        async with self._session as session:
            async with session.get(url) as response:
                ic(response.status)
                if response.status != 200:
                    return Err(f"Error fetching data. HTTP Status: {response.status}")
                data = await response.json()
                ic(data)
                return Ok(data)
