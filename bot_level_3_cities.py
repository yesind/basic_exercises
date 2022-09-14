import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random 
import settings
import pandas as pd

logging.basicConfig(filename='bot_level_3_cities.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\nДавай сыграем в города, набери /cities и добавь название города на русском языке.')

def cities_game(update, context):   #функция игры в города
    logging.info('Вызвана команда /cities') 
    user_word=update.message.text.split()[1:] #Берем список слов после /start
    logging.info(user_word)
    
    game_list = user_game_list(context.user_data)         #создаем пустой списк для игры       
    all_dic_cities = user_cities_list(context.user_data)
    all_cities = all_dic_cities.keys()    
    rest_all_cities=set(all_cities)-set(game_list) #вычисляем города, которые остались для игры
    user_word = " ".join([word.lower() for word in user_word]) # приводим к строчной первой букве введенный текст
    logging.info(game_list)   

    if user_word not in rest_all_cities:   # Проверяем первый раз ли вводится город
        update.message.reply_text("Вы вводили такое название города/Такого города нет") 
    elif len(game_list)>=1 and game_list[-1][-1]!=user_word.lower()[0] and (game_list[-1][-1] not in 'йьъы'): # Проверяем корректность первой буквы
        update.message.reply_text(f"Ваш город должен начинаться на {game_list[-1][-1].upper()}")
    elif len(game_list)>=1 and game_list[-1][-2]!=user_word.lower()[0] and (game_list[-1][-1] in 'йьъы'): # Проверяем корректность второй буквы
        update.message.reply_text(f"Ваш город должен начинаться на {game_list[-1][-2].upper()}")
    else:
        rest_all_cities.discard(user_word) # исключаем слово             !!!!!!!!!!!!!
        if user_word[-1] in 'йьъы': # выбираем на какую букву нужно искать слово и ищем слово
            bot_word=random.choice([city_letter for city_letter in rest_all_cities if city_letter[0].lower() == user_word[-2]])
        else:
            bot_word=random.choice([city_letter for city_letter in rest_all_cities if city_letter[0].lower() == user_word[-1]])                       
        game_list.append(bot_word) #добавлем слово в список игры
        update.message.reply_text(all_dic_cities[bot_word]) 

def user_game_list(user_data):
    if 'game_list' not in user_data:
        user_data['game_list']=[] 
    return user_data['game_list']

def user_cities_list(user_data):
    if 'cities_dict' not in user_data:
        file = pd.read_csv('city.csv')          #создаем список со всеми городами
        set_of_cities=file['city'].tolist()
        user_data['cities_dict']= {city.lower():city for city in set_of_cities} #создаем словарь городов пользователя !!!!!!!!!!
    return user_data['cities_dict']


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