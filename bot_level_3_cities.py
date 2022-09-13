import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random 
import settings
import pandas as pd

logging.basicConfig(filename='bot_level_3_cities.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\nДавай сыграем в города, набери /cities и добавишь название города на русском языке.')

def cities_game(update, context):   #функция игры в города
    logging.info('Вызвана команда /cities') 
    user_word=update.message.text.split()[1:] #Берем список слов после /start
    logging.info(user_word)
    
    game_list = user_game_list(context.user_data)         #создаем пустой списк для игры       
    all_cities = user_cities_list(context.user_data)
        
    rest_all_cities=set(all_cities)-set(game_list) #вычисляем города, которые остались для игры
    user_word = " ".join([word.capitalize() for word in user_word]) # приводим к заглавной первой букве введенный текст
    logging.info(game_list)
        

    if user_word not in rest_all_cities:   # Проверяем первый раз ли вводится город
        update.message.reply_text("Вы вводили такое название города") 
    elif len(game_list)>=1 and game_list[-1][-1]!=user_word.lower()[0] and (game_list[-1][-1] not in 'йьъы'): # Проверяем корректность первой буквы
        update.message.reply_text(f"Ваш город должен начинаться на {game_list[-1][-1]}")
    elif len(game_list)>=1 and game_list[-1][-2]!=user_word.lower()[0] and (game_list[-1][-1] in 'йьъы'): # Проверяем корректность второй буквы
        update.message.reply_text(f"Ваш город должен начинаться на {game_list[-1][-2]}")

    else:
        #game_list.append(user_word)   # добавляем слова для исклюючения
        rest_all_cities.discard(user_word) # исключаем слово

        user_word_lower = user_word.lower()

        if user_word[-1] in 'йьъы': # выбираем на какую букву нужно искать слово и ищем слово
            bot_word=random.choice([city_letter for city_letter in rest_all_cities if city_letter[0].lower() == user_word_lower[-2]])
        else:
            bot_word=random.choice([city_letter for city_letter in rest_all_cities if city_letter[0].lower() == user_word_lower[-1]])                       
        game_list.append(bot_word) #добавлем слово в список игры
        update.message.reply_text(bot_word) 

def user_game_list(user_data):
    if 'game_list' not in user_data:
        user_data['game_list']=[] 
    return user_data['game_list']

def user_cities_list(user_data):
    file = pd.read_csv('city.csv')          #создаем список со всеми городами
    user_data['cities_list']=file['city'].tolist()
    return user_data['cities_list']


def talk_to_me(update, context):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text[::-1])  

def main():
    mybot = Updater(settings.API_KEY, use_context = True) 
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()