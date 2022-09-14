import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot_level_3_calc.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\nЕсли ты введешь команду /calc и математическое выражение, то вычислю данное выражение')

def list_for_calc(string):
    all_list=[]
    for char in string:
        if char in '+/*-':
            index=string.index(char)
            all_list.append(float(string[:index]))
            all_list.append(char)
            string=string[index+1:]
    all_list.append(float(string))     
    return all_list

def string_calc(update, context):
    logging.info('Вызвана команда /calc')
    string_input=update.message.text.replace('/calc','').replace(' ','')  
   
    try: 
        if string_input[0] == "-":
            all_list=list_for_calc('0'+string_input)
        else:
            all_list=list_for_calc(string_input)

        while '*' in all_list or '/' in all_list:
            for i, char in enumerate(all_list):
                if str(char) in '/*':
                    if str(char) in '/':
                        try:
                            all_list[i-1]=all_list[i-1]/all_list[i+1]        
                        except ZeroDivisionError:
                            update.message.reply_text('Напоминаю, нельзя делить на ноль нельзя')
                    if str(char) in '*':
                        all_list[i-1]=all_list[i-1]*all_list[i+1]
                    all_list.pop(i+1)
                    all_list.pop(i)   
        
        while '+' in all_list or '-'in all_list:
            for i, char in enumerate(all_list):
                if str(char) in '-+':
                    if str(char) in '-':
                        all_list[i-1]=all_list[i-1]-all_list[i+1]        
                    if str(char) in '+':
                        all_list[i-1]=all_list[i-1]+all_list[i+1]
                    all_list.pop(i+1)
                    all_list.pop(i)        
        update.message.reply_text(all_list[0])
    except ValueError:
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