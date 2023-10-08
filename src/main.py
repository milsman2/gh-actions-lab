"""
This is the main entry point for the application.
"""
import asyncio

from icecream import ic
from pydantic import ValidationError
from result import Err, Ok

from src.schemas import SunResults
from src.client import AioHttpClient
from src.config import app_settings


async def get_sun_times() -> None:
    ic()
    async with AioHttpClient() as http_client:
        ic()
        results = await http_client.get_data(str(app_settings.TEST_URL))
        match results:
            case Ok(data):
                try:
                    SunResults(**data)
                except ValidationError as e:
                    ic(e)
                else:
                    ic(data)
                    ic(SunResults(**data))
            case Err(err):
                ic(err)


async def main():
    ic()
    await get_sun_times()


if __name__ == "__main__":
    ic()
    asyncio.run(main())
