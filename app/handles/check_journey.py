import asyncio
import aiohttp

# in this file i have to create somethin like a cron task to get journey updates every minute

async def check_journey(from_station, to_station):
    url = f'https://v5.db.transport.rest/journeys?from={from_station}&to={to_station}&results=1'
    async with aiohttp.ClientSession() as session:
        print('session')
        async with session.get(url) as response:
            print(session)
            if response.status == 200:
                data = await response.json()
                get_data = data["journeys"][0]["legs"]

                departure_time = get_data[0]["departure"]
                arrival_time = get_data[-1]["arrival"]
                departure_station = get_data[0]["origin"]['name']
                arrival_station = get_data[-1]['destination']['name']
                train_name = get_data[0]["line"]["name"]
                train_direction = get_data[0]["direction"]

   
                journey = data['journeys'][0]
                refresh_token = journey['refreshToken'] # ill use it later

                return {'departure_time': departure_time, 'arrival_time': arrival_time, 'departure_station': departure_station, 'arrival_station': arrival_station, 'train_name': train_name, 'train_direction': train_direction}
            else:
                print("Request failed with status code:", response.status)
            
        # async with session.get(f'https://v5.db.transport.rest/journeys/{refresh_token}') as refresh_resp:
        #     refresh_journey = await refresh_resp.json()
        #     print(refresh_journey.keys())
            # changes_detected = await check_journey_changes(journey, refresh_journey)
            # if changes_detected:
            #     print('Changes detected in the journey!')


