"""
This is the main entry point for the application.
"""
import asyncio

from icecream import ic
from pydantic import ValidationError
from result import Err, Ok, Result

from src.schemas import SunResults
from src.client import AioHttpClient
from src.config import app_settings


async def get_sun_times() -> Result[SunResults, str]:
    ic()
    async with AioHttpClient() as http_client:
        ic()
        results = await http_client.get_data(str(app_settings.TEST_URL))
        match results:
            case Ok(data):
                ic(type(data))
                try:
                    sun_data = SunResults(**data)
                except ValidationError as e:
                    ic(e)
                    return Err(str(e))
                else:
                    ic(sun_data)
                    return Ok(sun_data)
            case Err(err):
                ic(err)
                return Err(err)


async def main():
    ic()
    await get_sun_times()


if __name__ == "__main__":
    ic()
    asyncio.run(main())
