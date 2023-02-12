import datetime
from handles import get_location



async def generate_message(transfers):
    async def to_time(dt):
        result = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
        return result.strftime("%B %d, %H:%M")
    return f'Transfers - {len(transfers)-1}\n\n' + ''.join([f'<b>Train: {t["direction"]} - [{t["line"]["name"]}]</b>\nFrom: <b><a href={await get_location.get_maps_link(t["origin"]["name"])}>{t["origin"]["name"]}</a></b>\nTo: {t["destination"]["name"]}\nDeparture: <b>{await to_time(t["departure"])}</b>\nArrival: <b>{await to_time(t["arrival"])}</b>\n | \n' for t in transfers])