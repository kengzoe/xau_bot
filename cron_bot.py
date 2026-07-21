import logging, random, requests, asyncio
from telegram import Bot

TELEGRAM_TOKEN = "8927538018:AAFRkGtbi4iBrbKcdy7eu3jajLaSiYptW8A"
CHAT_ID = "YOUR_PERSONAL_TELEGRAM_CHAT_ID"  # Replace with your actual numerical chat ID
GOLDAPI_KEY = "ac6e6b5a-5bd1-4890-9b6d-5a6d279282c8"

logging.basicConfig(level=logging.INFO)

async def check_market_and_signal():
    url = "https://yahoo.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            live = res.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
            # Simulate a quick SMC matrix check
            if random.choice([True, False, False, False, False]):  # 20% random probability check for simulation
                bot = Bot(token=TELEGRAM_TOKEN)
                emoji = random.choice(["🚀 BUY", "🔻 SELL"])
                msg = f"{emoji} AUTOMATED PREMIUM SMC SETUP\n🎯 Asset: BTC-USD\n💵 Price Zone: ${live:.2f}\n📡 State: Telemetry Triggered"
                await bot.send_message(chat_id=CHAT_ID, text=msg)
                print("⚡ Signal generated and pushed successfully.")
    except Exception as e:
        print(f"Error executing scan matrix: {e}")

if __name__ == "__main__":
    asyncio.run(check_market_and_signal())
              
