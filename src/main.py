"""
This is the main entry point for the application.
"""
import asyncio

from icecream import ic
from pydantic import ValidationError
from result import Err, Ok, Result

from schemas.sun_results import SunResults
from client.aiohttp_client import AioHttpClient
from config.settings import Settings


async def get_sun_times() -> Result[SunResults, str]:
    ic()
    settings = Settings()
    async with AioHttpClient() as http_client:
        ic()
        data = await http_client.get_data(str(settings.TEST_URL))
        match data:
            case Ok(data):
                ic(data)
            case Err(err):
                ic(err)
        try:
            SunResults(**data)
        except ValidationError as e:
            ic(f"Error parsing data: {e}")
        else:
            ic(SunResults(**data))


async def main():
    ic()
    await get_sun_times()


if __name__ == "__main__":
    ic()
    asyncio.run(main())
