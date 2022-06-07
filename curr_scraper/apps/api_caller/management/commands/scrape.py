from django.core.management.base import BaseCommand
from api_caller.models import RateRecord
from dotenv import load_dotenv
from datetime import datetime
import requests
import os
import json
import pytz

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    help = 'Scrapes openexchangerates for currency rates.'
    url = os.environ.get("URL")
    timestamp = None
    try:
        response = requests.get(url)
        json_data = json.loads(response.text)
        timestamp = json_data["timestamp"]
        rates = json_data["rates"]
    except KeyError:
        # send error to sentry
        print("Key Error")
    else:
        UAH = rates["UAH"]
        GBP = rates["GBP"]
        PLN = rates["PLN"]
        EUR = rates["EUR"]

    if timestamp is not None:
        tz = pytz.timezone("Europe/Kiev")
        timestampz = datetime.fromtimestamp(timestamp, tz)
        record = RateRecord(timestamp=timestampz, UAHrate=UAH, GBPrate=GBP, PLNrate=PLN, EURrate=EUR)
        record.save()
