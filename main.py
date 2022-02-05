from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
#<<<======Variable Declaration========>>>#
TOKEN="1963665302:AAFKNH7N7LBZpdQAsZKi-RVXgDqB1w1oosU"
updater = Updater(TOKEN, use_context=True)
#replies:-
helpText="""
=============================
command             usage
----------------------------------------------------------
/help            |- for this help menu.
/github        |- BHUTUU's github 👻.
/website     |- BHUTUU's website.
/youtube     |- BHUTUU's youtube
/webclock  |- To open WebClock
/calculator |- To open calculator
/star            |- To see stars ;)
______________________________________
"""

#<<<======Function Declaration=========>>>#
#def expl(update: Update, context: CallbackContext):
#    word=update.message.text.split(' ')[1]
#    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("""Hello sir, Welcome to the Bot.Please write /help to see the commands available.""")
def help(update: Update, context: CallbackContext):
    update.message.reply_text(helpText)
def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("""https://github.com/BHUTUU""")
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("""https://www.youtube.com/channel/UCcbIIYUlcfjkYLHQ5EklztA""")
def website_url(update: Update, context: CallbackContext):
    update.message.reply_text("""bhutuu.github.io""")
def calculator_url(update: Update, context: CallbackContext):
    update.message.reply_text("""bhutuu.github.io/calculator""")
def shootingStar_url(update: Update, context: CallbackContext):
    update.message.reply_text("""bhutuu.github.io/shootingStar""")
def clockGui_url(update: Update, context: CallbackContext):
    update.message.reply_text("""bhutuu.github.io/clockgui""")
#def unknown(update: Update, context: CallbackContext):
#    update.message.reply_text("""Sorry '%s' is not a valid command""" % update.message.text)
#def unknown_text(update: Update, context: CallbackContext):
#    update.message.reply_text("""Sorry I can't recognize you , you said '%s'""" % update.message.text)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('star', shootingStar_url))
updater.dispatcher.add_handler(CommandHandler('webclock', clockGui_url))
updater.dispatcher.add_handler(CommandHandler('calculator', calculator_url))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
#updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()
