import json
import pytz
import requests

from datetime import datetime
from django.conf import settings
from api_caller import models



def call_api():
    """Make a call to API, check response, and return json data. Return None if was not able to fetch a valid JSON"""
    oe_url = settings.OPEN_EXCHANGE_URL
    oe_app_id = settings.OPEN_EXCHANGE_APP_ID
    oe_complete_url = f'{oe_url}/latest.json?app_id={oe_app_id}'
    try:
        response = requests.get(oe_complete_url)
    except requests.ConnectionError:
        print("Connection Error!")
    except requests.HTTPError:
        print("Unsuccessful status code")
    except requests.Timeout:
        print("Connection timed out")
    except requests.TooManyRedirects:
        print("Exceeded maximum amount of redirects")
    try:
        json_data = json.loads(response.text)
    except json.JSONDecodeError:
        print("Response is not a JSON")
    try:
        base = json_data["base"]
    except KeyError:
        print("JSON has wrong data")
    else:
        return json_data
    return None

def initialize_currency_table():
    """Take json data and initialize the currency table with currency codes"""
    json_data = call_api()
    if json_data:
        rates = json_data["rates"]
        curr_list = rates.keys()
        for currency in curr_list:
            cr = models.Currency(code=currency, description=currency)
            cr.save()


def scrape_data(base_currency="USD"):
    """Take json data and populate currency rate table with new info"""
    json_data = call_api()
    timestamp = json_data["timestamp"]
    rates = json_data["rates"]
    curr_list = rates.keys()
    if base_currency == "USD":
        pass
    elif base_currency in curr_list:
        base_rate = curr_list[base_currency]
        for currency in curr_list:
            rates[currency] = rates[currency]/base_currency
    else:
        print("Currency not found")
        return
    tz = pytz.timezone("Europe/Kiev")
    timestampz = datetime.fromtimestamp(timestamp, tz)



        

