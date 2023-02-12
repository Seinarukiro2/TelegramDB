
import aiohttp

from handles import get_location, generator

# in this file i have to create somethin like a cron task to get journey updates every minute

async def check_journey(from_station, to_station):
    url = f"https://v5.db.transport.rest/journeys?from={from_station}&to={to_station}&results=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                
                data = await response.json()

                transfers = data["journeys"][0]["legs"]

                return await generator.generate_message(transfers=transfers)
            else:
                return f"Request failed with status code: {response.status}"





