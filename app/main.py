from telethon import TelegramClient, events
import config

from handles import get_station_info, check_journey, encoder

# api connection
client = TelegramClient('bot', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
client.parse_mode = "html"


@client.on(events.NewMessage(pattern=r'^(/start)')) # start bot command handler
async def my_status(event):
    await event.respond(f"Welcome to Deutsche Bahn Telegram Bot")


@client.on(events.NewMessage(pattern=r'^(!)')) # it is just test func (delete/change)
async def my_status(event):
    
    a = event.text.split(" ")
    if len(a) < 0:
        await event.respond(f"Parameters is not correct")
        return
    print(a[1])
    await event.respond(f"{await get_station_info.get_data(a[1])}")


@client.on(events.NewMessage(pattern=r'^(/)')) # basic journey info returner
async def my_status(event):
    a = event.text.split(" ")
    print(await encoder.convert_to_german_chars(a[1]))
    from_id = await get_station_info.get_data(await encoder.convert_to_german_chars(a[1]))
    to_id = await get_station_info.get_data(await encoder.convert_to_german_chars(a[2]))
    print(from_id, to_id)
    # data = await check_journey.check_journey(from_id, to_id)

    # await event.respond(f"{data['departure_time']}\n{data['departure_station']}\n{data['train_name']}\n{data['arrival_station']}")
    await event.respond(await check_journey.check_journey(from_id, to_id))

client.start()
client.run_until_disconnected() 