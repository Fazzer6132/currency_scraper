import json
import pytz
import requests

from datetime import datetime
from django.conf import settings
from api_caller import models



def call_api():
    """Make a call to API, check response, and return json data. Return None if was not able to fetch a valid JSON"""
    oe_url = settings.OE_URL
    oe_app_id = settings.OE_APP_ID
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
            cr = models.Currency.objects.get_or_create(code=currency, description=currency)


def scrape_data(base_currency="USD"):
    """Take json data and populate currency rate table with new info"""
    json_data = call_api()
    if json_data:
        timestamp = json_data["timestamp"]
        rates = json_data["rates"]
        curr_list = rates.keys()
        if base_currency == "USD":
            pass
        elif base_currency in curr_list:
            base_rate = rates[base_currency]
            for currency in curr_list:
                rates[currency] = rates[currency]/base_rate
        else:
            print("Currency not found")
            return
        tz = pytz.timezone("Europe/Kiev")
        timestampz = datetime.fromtimestamp(timestamp, tz)
        c_list = models.Currency.objects.all()
        base_currency_id = c_list.filter(code=base_currency).first()
        for currency in curr_list:
            currency_id = c_list.filter(code=currency).first()
            curr_rate_record = models.CurrencyRateRecord(timedate=timestampz, curr=currency_id, base_curr=base_currency_id, rate=rates[currency])
            curr_rate_record.save()


        

