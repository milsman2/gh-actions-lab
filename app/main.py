"""
Docstring for main.py
"""
import aiohttp
import asyncio
from result import Ok, Err, Result
from schemas.sun_results import SunResults
from pydantic import ValidationError
from config.settings import Settings
from icecream import ic, install


async def get_sun_times() -> Result[SunResults, str]:
    settings = Settings()
    async with aiohttp.ClientSession() as session:
        async with session.get(str(settings.TEST_URL)) as response:
            if response.status != 200:
                return Err(f"Error fetching data. HTTP Status: {response.status}")
            data = await response.json()
            try:
                SunResults(**data)
            except ValidationError as e:
                return Err(f"Error parsing data: {e}")
            else:
                return Ok(SunResults(**data))


async def main():
    install()
    result = await get_sun_times()
    match result:
        case Ok(data):
            ic(data)
        case Err(error):
            ic(error)


if __name__ == "__main__":
    asyncio.run(main())
