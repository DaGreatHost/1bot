import telebot
from telebot import types
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
REQUIRED_CHANNEL_ID = int(os.environ.get("REQUIRED_CHANNEL_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

def is_user_joined(chat_member):
    return chat_member.status in ['member', 'creator', 'administrator']

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    username = '@' + user.username if user.username else user.first_name

    caption = f"{username} forward (0/5)\n\nWag kalimutang mag ambag\n\n👉 <a href='https://t.me/forwardtutorial1'>PAANO MAG FORWARD</a>"
    photo = open('media/123.jpg', 'rb')

    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("Boso GC", callback_data="boso_gc"))
    markup.row(
        types.InlineKeyboardButton("Join", url="https://tgreward.shop/join.php"),
        types.InlineKeyboardButton("Avail VIP", url="https://t.me/trendsmodbot")
    )

    bot.send_photo(message.chat.id, photo=photo, caption=caption, parse_mode="HTML", reply_markup=markup)
    photo.close()

@bot.callback_query_handler(func=lambda call: call.data == "boso_gc")
def handle_boso_gc(call):
    user_id = call.from_user.id
    try:
        chat_member = bot.get_chat_member(REQUIRED_CHANNEL_ID, user_id)

        if is_user_joined(chat_member):
            bot.answer_callback_query(call.id, "✅ Welcome sa Boso GC!")
        else:
            raise Exception("Not joined")

    except:
        bot.answer_callback_query(call.id, "Opps , please JOIN ✅ first!", show_alert=True)

bot.polling()
