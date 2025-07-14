from telegram.ext import Updater, CommandHandler
import requests

BOT_TOKEN = '7324799687:AAEw5jlN8mzaxI27lNBlSRgabfeszs4Xs8o'

def get_signal(symbol='BTCUSDT'):
    symbol = symbol.upper()
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"

    try:
        data = requests.get(url).json()

        price = float(data['lastPrice'])
        change = float(data['priceChangePercent'])

        if change > 2:
            signal = "🟢 Strong BUY"
            buy = 80
            sell = 20
            entry = price
            target = round(price * 1.02, 2)
            sl = round(price * 0.985, 2)

        elif change < -2:
            signal = "🔴 Strong SELL"
            buy = 20
            sell = 80
            entry = price
            target = round(price * 0.98, 2)
            sl = round(price * 1.015, 2)

        else:
            signal = "🟡 Neutral / Sideways"
            buy = 50
            sell = 50
            entry = price
            target = "-"
            sl = "-"

        return f"""📊 *{symbol} Signal*
💰 Price: ${price}
📈 24h Change: {change}%
🔼 Buy Chance: {buy}%
🔽 Sell Chance: {sell}%
🧠 Signal Strength: {signal}

🎯 Entry: ${entry}
🎯 Target: {target}
🛑 Stoploss: {sl} 
"""
    except:
        return f"❌ Invalid symbol or Binance API error. Try like: `/trade btcusdt`"

def trade(update, context):
    args = context.args
    symbol = args[0].upper() if args else 'BTCUSDT'
    result = get_signal(symbol)

    # Monetag link add
    full_message = result + "\n\n💹 *Want full chart & bonus signals?*\n🔗 [Open Signal Page](https://cryptosignalmonetag.netlify.app)"

    update.message.reply_text(full_message, parse_mode='Markdown')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("trade", trade))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
