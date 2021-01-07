import requests, gevent

requests.adapters.DEFAULT_RETRIES = 2


def get_time(timestamp):
    print(f'Requesting for server time by IP at {timestamp}')
    thread = gevent.spawn(requests.get, 'https://worldtimeapi.org/api/ip')
    thread.join()
    return thread.value.json()