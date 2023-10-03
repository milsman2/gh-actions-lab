"""
This is the main entry point for the application.
"""
import asyncio

import aiohttp
from icecream import ic, install
from pydantic import ValidationError
from result import Err, Ok, Result

from src.config.settings import Settings
from src.schemas.sun_results import SunResults


async def get_sun_times() -> Result[SunResults, str]:
    ic()
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
    ic()
    result = await get_sun_times()
    match result:
        case Ok(sun_results):
            ic(sun_results.model_dump_json(indent=2))
        case Err(error):
            ic(error)


if __name__ == "__main__":
    asyncio.run(main())
