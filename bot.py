
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("👋 Welcome to Trade Signal Bot!\nVisit for full analysis: https://cryptosignalmonetag.netlify.app")

updater = Updater("7324799687:AAEw5jlN8mzaxI27lNBlSRgabfeszs4Xs8o", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
