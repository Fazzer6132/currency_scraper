import os
from datetime import datetime
import json
import pytz
import requests
from curr_scraper.apps.api_caller.models import Currency, CurrencyRateRecord


def call_api():
    oe_url = os.environ.get('OPEN_EXCHANGE_URL')
    oe_app_id = os.environ.get('OPEN_EXCHANGE_APP_ID')
    oe_complete_url = f'{oe_url}/latest.json?app_id={oe_app_id}'
    try:
        response = requests.get(oe_complete_url)
        json_data = json.loads(response.text)
        base = json_data["base"]
    except KeyError:
        print("KeyError")
    else:
        return json_data


def initialize_currency_table():
    json_data = call_api()
    rates = json_data["rates"]
    curr_list = rates.keys()
    for currency in curr_list:
        cr = Currency(code=currency, description=currency)
        cr.save()


def scrape_data(base_currency):
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

        

