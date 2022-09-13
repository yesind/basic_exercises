import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot_level_3_calc.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\nЕсли ты введешь команду /calc и математическое выражение, то вычислю данное выражение')

def string_calc(update, context):
    logging.info('Вызвана команда /calc')
    string_input=update.message.text.split()[1:]
    string=''.join(string_input)
    logging.info(string)
    try: 
        update.message.reply_text(eval(string))
    except ZeroDivisionError:
        update.message.reply_text('Напоминаю, нельзя делить на ноль нельзя')
    except (SyntaxError,NameError):
        update.message.reply_text('Калькулятор не понимает буквы')     

def talk_to_me(update, context):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text[::-1])  

def main():
    mybot = Updater(settings.API_KEY, use_context = True) 
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("calc", string_calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()