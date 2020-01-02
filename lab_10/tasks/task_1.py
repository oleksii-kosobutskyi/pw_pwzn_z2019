import requests
from urllib.parse import urljoin
from json import JSONDecodeError


API_URL = 'https://www.metaweather.com/api/'


def get_cities_woeid(query: str, timeout: float = 5.0):

    location_url = urljoin(API_URL, 'location/search')
    try:
        response = requests.get(location_url, params={'query': query}, timeout=timeout)
    except requests.exceptions.Timeout:
        raise
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise
    try:
        cities = response.json()
    except JSONDecodeError:
        raise RuntimeError

    output = {}
    for city in cities:
        output[city['title']] = city['woeid']
    return output


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
