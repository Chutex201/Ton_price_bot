import requests
import time
from telegram import Bot

# ========== CONFIG ==========

TOKEN = "8574530686:AAHnl9Q3GkTreO_yGZYpr9p9d0atd8hiTho"  # Replace with your BotFather token
CHANNEL = "@lonerRoad"  # Replace with your channel username

bot = Bot(token=TOKEN)

# ========== FUNCTION TO GET TON PRICE ==========
def get_ton_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"
    try:
        data = requests.get(url).json()
        price = data["the-open-network"]["usd"]
        return price
    except:
        return None

# ========== MAIN LOOP ==========
while True:
    price = get_ton_price()
    if price:
        message = f"💎 <b>TON (Stone) Live Price</b>\n\n💰 Price: ${price}\n⏱ Updated every 5 minutes"
        bot.send_message(chat_id=CHANNEL, text=message, parse_mode="HTML")
    time.sleep(300)  # 5 minutes