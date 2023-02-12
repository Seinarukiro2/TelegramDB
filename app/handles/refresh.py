import asyncio
import aiohttp

from handles import generator

async def check_something(client, message, from_id, to_id, event):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://v5.db.transport.rest/journeys?from={from_id}&to={to_id}&results=1") as response:
            data = await response.json()
            journey = data['journeys'][0]
            refresh_token = journey['refreshToken']
            async with session.get(f'https://v5.db.transport.rest/journeys/{refresh_token}') as refresh_resp:
                refresh_journey = await refresh_resp.json()
            transfers = data["journeys"][0]["legs"]
            refresh_transfers = refresh_journey["legs"]
            transfers_text = await generator.generate_message(transfers=transfers)
            refresh_transfers_text = await generator.generate_message(transfers=refresh_transfers)

            if transfers_text != refresh_transfers_text:
                await client.edit_message(event.sender.id, message.id, refresh_transfers_text)

task_running = False

async def cron_task(client, message, from_id, to_id, event):
    global task_running
    if task_running:
        task_running.cancel()
        await task_running
        task_running = None
    
    stop_time = asyncio.get_running_loop().time() + 24 * 3600
    task_running = asyncio.create_task(run_task(client, message, from_id, to_id, event, stop_time))

async def run_task(client, message, from_id, to_id, event, stop_time):
    try:
        while asyncio.get_running_loop().time() < stop_time:
            await asyncio.sleep(60)
            await check_something(client=client, message=message, from_id=from_id, to_id=to_id, event=event)
    except asyncio.CancelledError:
        pass
