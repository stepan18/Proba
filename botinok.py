from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes, CallbackContext

# Токен от BotFather
TOKEN = '8258969497:AAHjfDcVhSBBXL11rY8ldR-0heDvDlcITNw'

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот с меню. Напиши /menu, чтобы открыть меню ссылок!')

# Обработчик команды /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаём кнопки с URL-ссылками
    keyboard = [[InlineKeyboardButton("Паша", callback_data="action1")], [InlineKeyboardButton("Лиза", callback_data="action2")], [InlineKeyboardButton("Старый", callback_data="action3")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с меню
    await update.message.reply_text('Выберите ссылку:', reply_markup=reply_markup)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Подтверждаем получение callback

    if query.data == "action1":
        await Pasha(query, context)
    elif query.data == "action2":
        await Liza(query, context)
    elif query.data == "action3":
        await Ded(query, context)

async def Pasha(query: Update.callback_query, context: ContextTypes.DEFAULT_TYPE) -> None:
    await query.message.reply_text("Паша сосал!")
    await menu(query, context)

async def Liza(query: Update.callback_query, context: ContextTypes.DEFAULT_TYPE) -> None:
    await query.message.reply_text("Красотка❤️")
    await menu(query, context)

async def Ded(query: Update.callback_query, context: ContextTypes.DEFAULT_TYPE) -> None:
    await query.message.reply_text("ЛОХ!")
    await menu(query, context)

async def MetaData(query: Update.callback_query, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = query.message.from_user
    user_id = user.id
    name = user.first_name
    username = user.username
    await query.message.reply_text(f'Ваш тг id: {user_id}\n Ваш никнейм: {name}\n Имя пользователя: @{username}')

def main() -> None:
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("meta", MetaData))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()