import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta
import asyncio


from get_prayer_time import get_prayer_time
from ask_question import ask_question

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Le bot marche")
    await bot.tree.sync()
    prayer_time_notification.start()



@tasks.loop(minutes=1)  
async def prayer_time_notification():
    now = datetime.now().strftime('%H:%M')
    timings = get_prayer_time()

    channel = bot.get_channel(1101938838177333401) 

    if channel is None:
        print(f"Le canal avec l'ID {1101938838177333401} est introuvable.")
        return

    for prayer, time in timings.items():
        
        prayer_time = datetime.strptime(time, '%H:%M').strftime('%H:%M')

        if now == prayer_time:
            await channel.send(f"@everyone Il est maintenant l'heure de prier ({prayer})")
        
        if prayer == "Imsak":
            break


            
@bot.hybrid_command(name="prayertime", with_app_command=True, description="Affiche les heures de prière d'aujourd'hui")
async def prayertime(ctx):
    timings = get_prayer_time()
    embeded_message = discord.Embed(title="Horaires de prière", description=f"Voici les horaires de prière pour le {datetime.now().strftime('%d-%m-%Y')}")
    embeded_message.set_thumbnail(url=ctx.author.avatar)
    embeded_message.add_field(name="Fajr", value=timings["Fajr"])
    embeded_message.add_field(name="Sunrise", value=timings["Sunrise"])
    embeded_message.add_field(name="Dhuhr", value=timings["Dhuhr"])
    embeded_message.add_field(name="Asr", value=timings["Asr"])
    embeded_message.add_field(name="Maghrib", value=timings["Maghrib"])
    embeded_message.add_field(name="Isha", value=timings["Isha"])

    await ctx.send(embed=embeded_message)

@bot.hybrid_command(name="question", with_app_command=True, description="Ask me any question related to Islam")
@app_commands.describe(query="The question you want to ask")
async def askquestion(ctx, query):
    await ctx.defer()  # This defers the interaction response, preventing a timeout
    response = ask_question(query)
    await ctx.send(response)



bot.run(os.getenv('TOKEN'))
