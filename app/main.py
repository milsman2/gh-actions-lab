"""
Docstring for main.py
"""
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.sunrisesunset.io/json?lat=29.7604&lng=-95.3698&timezone=UTC&date=today"
        ) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])
            html = await response.text()
            print(html)


if __name__ == "__main__":
    asyncio.run(main())
