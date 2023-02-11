import aiohttp
import asyncio

async def get_maps_link(station):
    url = f'https://v5.db.transport.rest/locations?query={station}&results=1'
    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            if response.status == 200:
                data = await response.json()
                latitude = data[0]['location']['latitude']
                longitude = data[0]['location']['longitude']
                google_maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
                return google_maps_link
                
            else:
                
                print("Request failed with status code: ", response.status)
                return "Server error"


