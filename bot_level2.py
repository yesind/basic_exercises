import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings
from datetime import datetime
logging.basicConfig(filename='bot.log', level=logging.INFO)



def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def len_string(update, context):
    logging.info('Вызвана команда /wordcount')
    string=update.message.text.split()[1:]
    if string: 
        update.message.reply_text(f'Фраза состоит из {len(string)} слов(а)')
    else:
        update.message.reply_text("Вы указали пустую строку")

def full_moon(update, context):
    logging.info('Вызвана команда /next_full_moon')
    s=update.message.text.split()[1]
    try: 
        date=datetime.strptime(update.message.text.split()[1], '%d/%m/%Y')
    except ValueError:
        update.message.reply_text("Вы указали некорректную дату")
        update.message.reply_text("Корректный запрос /next_full_moon DD/MM/YYYY")   
    
    update.message.reply_text(s)
    update.message.reply_text(f'Следующие полнолуние {ephem.next_full_moon(date)}')
    

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True) 
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", len_string))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
