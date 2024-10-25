import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime

def get_prayer_time():
    
    today_date = datetime.now().strftime('%d-%m-%Y')
    
    url = f"http://api.aladhan.com/v1/timings/{today_date}?latitude=36.75587&longitude=5.08433&method=3"

    
    
    
    response = requests.get(url)
    data = response.json()



    timings = data['data']['timings']
    return timings


prayer_times = get_prayer_time()
print(json.dumps(prayer_times, indent=4))
