import discord
import logging
from bs4 import BeautifulSoup
import requests
import datetime
from webserver import keep_alive


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

list_of_jks = [
    "Did you hear about the mathematician who’s afraid of negative numbers?\n He’ll stop at nothing to avoid them.",
    "Why do we tell actors to “break a leg?\nBecause every play has a cast.",
    "Hear about the new restaurant called Karma\nThere’s no menu: You get what you deserve.",
    "A man tells his doctor, “Doc, help me. I’m addicted to Twitter!the doctor replies,\n “Sorry, I don’t follow you …”",

]


def get_price_of_coin(coin_type):
    url = f'https://coinmarketcap.com/'

    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    my_div = soup.find('a', {'href': f'/currencies/{coin_type}/markets/'}).get_text()

    return my_div


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


counter = 0


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):

        if message.content.startswith("$hello"):
            await message.channel.send(f'hello {message.author.name}!')

        if message.content.startswith("$whats your name") and message.author.name == "sire":
            await message.channel.send(f'My name is zeek , sire.')

        elif message.content.startswith("$whats your name") and message.author.name != "sire":
            await message.channel.send(f'I am zeek, {message.author.name}.')

        if message.content.startswith("$what is BTC price"):
            await message.channel.send(
                f'price of btc at {datetime.datetime.now()} is:\n {get_price_of_coin("bitcoin")}')

        elif message.content.startswith('$what is ETH price'):
            await message.channel.send(
                f'price of eth at {datetime.datetime.now()} is:\n {get_price_of_coin("ethereum")}')

        if message.content.startswith('$tell me a joke'):
            global counter
            if counter < 3:
                counter += 1
            elif counter >= 3:
                counter = 0

            await message.channel.send(f'```{list_of_jks[counter]}```')

        if message.content.startswith('$that was dry') and message.author.name == "sire":
            await message.channel.send("okay :(")

        elif message.content.startswith('$that was dry') and message.author.name != "sire":
            await message.channel.send("like your humour")
        
        if message.content.startswith('$get entire price chart'):
            await message.channel.send(f'```Bitcoin -> {get_price_of_coin("bitcoin")}\n'
                                            f'Ethereum -> {get_price_of_coin("ethereum")}\n'
                                            f'Dogecoin -> {get_price_of_coin("dogecoin")}\n'
                                            f'XRP -> {get_price_of_coin("xrp")}\n'
                                            f'Binance-coin -> {get_price_of_coin("binance-coin")}\n'
                                            '```')
        
        if message.content.startswith("$commands"):
          await message.channel.send(f"```$hello -> greets you\n"
                                       "$whats your name -> tells name\n"
                                       "$what is BTC price -> scrapes ETH price\n"
                                       "$what is ETH price -> scrapes ETH price \n"
                                       "$tell me a joke -> tells a joke \n"
                                       "$get entire price chart -> gets entire crypto price chart```")


keep_alive()

with open("token.env", "r") as file:
  TOKEN = file.read()

client.run(TOKEN)

