from telegram.ext import Updater, CommandHandler
import imghdr

def start(update, context):
    update.message.reply_text("Hello! I’m alive with imghdr 😎")

def main():
    TOKEN = "7324799687:AAEw5jlN8mzaxI27lNBlSRgabfeszs4Xs8o"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
