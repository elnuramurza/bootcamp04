import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
 
# Введите токен своего бота
TOKEN = "6356346658:AAFi_3pY-PWWf_M627gTUzADDv2nhftBEB4"
 
# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
 
logger = logging.getLogger(__name__)
 
# Обработка команды /start
def start(update: Update, context: CallbackContext) -&gt; None:
    update.message.reply_text('Привет, я твой телеграм-бот! 😊')
 
# Обработка текстовых сообщений
def echo(update: Update, context: CallbackContext) -&gt; None:
    update.message.reply_text(f'Вы написали: {update.message.text}')
 
# Главная функция
def main() -&gt; None:
    updater = Updater(TOKEN)
 
    dispatcher = updater.dispatcher
 
    # Регистрация обработчиков
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text &amp; ~Filters.command, echo))
 
    # Запуск бота
    updater.start_polling()
    updater.idle()
 
if __name__ == '__main__':
    main()