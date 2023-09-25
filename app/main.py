"""
Docstring for main.py
"""
import aiohttp
import asyncio
from result import Ok, Err, Result
from schemas.sun_results import SunResults
from pydantic import ValidationError


async def get_sun_times() -> Result[SunResults, str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=UTC&date=today"
        ) as response:
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
    result = await get_sun_times()
    match result:
        case Ok(data):
            print(data)
        case Err(error):
            print(error)


if __name__ == "__main__":
    asyncio.run(main())
