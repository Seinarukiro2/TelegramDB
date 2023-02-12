import os
from telethon import TelegramClient, events
import config # U have to create this file with TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN

from handles import get_station_info, check_journey, encoder, refresh


# api connection
client = TelegramClient('bot', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH) 
client.parse_mode = "html"

async def handle_command(event):
    if event.text.startswith("/start"):
        await event.respond("Welcome to Deutsche Bahn Telegram Bot")
    elif event.text.startswith("/ "): # it was a technical function, ill change it in the future
        a = event.text.split(" ")
        if len(a) < 2:
            await event.respond("Parameters are not correct")
            return
        await event.respond(f"{await get_station_info.get_data(a[1])}")
    elif event.text.startswith("!"): # here i have to change split to (maybe re) idk
        a = event.text.split(" ")
        if len(a) < 3:
            await event.respond("Parameters are not correct")
            return
        from_id = await get_station_info.get_data(await encoder.convert_to_german_chars(a[1]))
        to_id = await get_station_info.get_data(await encoder.convert_to_german_chars(a[2]))
        message = await event.respond(await check_journey.check_journey(from_id, to_id))
        
        await refresh.cron_task(client=client, message=message, from_id=from_id, to_id=to_id, event=event)

@client.on(events.NewMessage)
async def handler(event):
    await handle_command(event)

client.start(bot_token=config.BOT_TOKEN)
client.run_until_disconnected()