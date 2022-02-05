from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
#<<<======Variable Declaration========>>>#
TOKEN="1963665302:AAFKNH7N7LBZpdQAsZKi-RVXgDqB1w1oosU"
updater = Updater(TOKEN, use_context=True)
#replies:-
helpText="""
=============================
command             usage
----------------------------------------------------------
/help     |- for this help menu.
/say      |- only for BHUTUU 👻.
/fetch   |- To fetch sysinfo.
/battery|- To fetch battery.
______________________________________
"""

#<<<======Function Declaration=========>>>#
def define(update: Update, context: CallbackContext):
    word=update.message.text
    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
    parseJson=json.loads(response)
    update.message.reply_text(parseJson["definiton"])
def start(update: Update, context: CallbackContext): 
    update.message.reply_text("""Hello sir, Welcome to the Bot.Please write /help to see the commands available.""") 
def help(update: Update, context: CallbackContext): 
    update.message.reply_text(helpText) 
def gmail_url(update: Update, context: CallbackContext): 
    update.message.reply_text("""Your gmail link here (I am not\ 
        giving mine one for security reasons)""")
def youtube_url(update: Update, context: CallbackContext): 
    update.message.reply_text("""Youtube Link => https://www.youtube.com/""") 
def linkedIn_url(update: Update, context: CallbackContext): 
    update.message.reply_text("""LinkedIn URL => https://www.linkedin.com/in/dwaipyan-bandyopadhyay-007a/""")
def geeks_url(update: Update, context: CallbackContext): 
    update.message.reply_text("""GeeksforGeeks URL => https://www.geeksforgeeks.org/""") 
def unknown(update: Update, context: CallbackContext): 
    update.message.reply_text("""Sorry '%s' is not a valid command""" % update.message.text) 
def unknown_text(update: Update, context: CallbackContext): 
    update.message.reply_text("""Sorry I can't recognize you , you said '%s'""" % update.message.text)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url)) 
updater.dispatcher.add_handler(CommandHandler('help', help)) 
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url)) 
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url)) 
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url)) 
updater.dispatcher.add_handler(CommandHandler('define', define))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown)) 
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling() 
