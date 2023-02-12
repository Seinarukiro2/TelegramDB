import aiohttp

# i should to change this file it is so bad

async def get_id(station_json): # json of this API is so strange so i have to use this function 
    first_key, _ = next(iter(station_json.items()))
    return first_key


async def get_data(station_name):
    url = f"https://v5.db.transport.rest/stations?query={station_name}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                first_key = await get_id(data)
                return data[first_key]['id'] #  it have to be a normal data about station (but rn its just a id)

            else:
                print("Request failed with status code:", response.status)


