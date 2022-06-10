import os
from datetime import datetime
import json
import pytz
import requests
import models


def scrape_data(base_currency):
    oe_url = os.environ.get('OPEN_EXCHANGE_URL')
    oe_app_id = os.environ.get('OPEN_EXCHANGE_APP_ID')
    oe_complete_url = f'{oe_url}/latest.json?app_id={oe_app_id}'
    timestamp = None
    try:
        response = requests.get(oe_complete_url)
        json_data = json.loads(response.text)
        timestamp = json_data["timestamp"]
    except KeyError:
        print("KeyError")
    else:
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
        

