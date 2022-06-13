import json
import os
from datetime import datetime

import pytz
import requests
from .api_caller import call_logic
from django.core.management.base import BaseCommand




class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    call_logic.scrape_data()

