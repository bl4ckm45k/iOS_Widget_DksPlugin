from typing import Tuple
from loader import redis_cli
import datetime


def timedelta_to_dhms(duration) -> Tuple:
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds


def check_map(map_name: str) -> bool:
    if any(x == map_name[0] for x in ['4', '5']): return False
    if map_name[0:2] == 'GG': return False
    if map_name[-2:] == 'BL': return False
    if 'Blacklight' in map_name: return False
    return True


async def process_data(dictionary: dict) -> dict:
    uri_alert = False if await redis_cli.get(f'uri_alert:{dictionary["hero"]["id"]}') is None else True
    if check_map(dictionary['map']['name']):
        if len(dictionary['plugin']['liveLogs']['lastStdLogs']) > 0:
            current_time = datetime.datetime.now()
            for info in dictionary['plugin']['liveLogs']['lastStdLogs']:
                str_log_time = info[1:20]
                date_object = datetime.datetime.strptime(str_log_time, '%Y-%m-%d %H:%M:%S')
                days, hours, minutes, seconds = timedelta_to_dhms(current_time - date_object)
                if any(x > 0 for x in [days, hours, minutes]):
                    break
                info = info[22:].strip()
                if 'URI!' in info:
                    _, amount_uri = info.replace(' URI!', '').strip().split()
                    amount_uri = int(amount_uri.replace('.', ''))
                    if amount_uri % 2 != 0 and amount_uri < 5000:
                        if not uri_alert:
                            uri_alert = True
                            await redis_cli.set(f'uri_alert:{dictionary["hero"]["id"]}', '1', ex=300)
    new_data = {
        "hero": {
            "username": dictionary["hero"]["username"]
        },
        "map": dictionary["map"]["name"],
        "stats": {
            "runningTime": dictionary["stats"]["runningTime"],
            "totalUridium": dictionary["stats"]["totalUridium"],
            "uridiumPerHour": int(
                (dictionary["stats"]["earnedUridium"] / dictionary["stats"]["runningTimeSeconds"]) * 3600)
        },
        "alert": uri_alert
    }
    return new_data
