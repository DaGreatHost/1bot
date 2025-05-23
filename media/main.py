
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

def is_user_joined(chat_member):
    return chat_member.status in ['member', 'creator', 'administrator']

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    username = '@' + user.username if user.username else user.first_name

    caption = f"{username} forward (0/5)\n\nWag kalimutang mag ambag\n\n👉 [PAANO MAG FORWARD](https://t.me/forwardtutorial1)"
    photo = open('media/123.jpg', 'rb')

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Boso GC", callback_data="boso_gc"))
    markup.add(types.InlineKeyboardButton("Join", url="https://t.me/+0enGe_F5qDg1ODg1"))

    bot.send_photo(message.chat.id, photo=photo, caption=caption, parse_mode="Markdown", reply_markup=markup)
    photo.close()

@bot.callback_query_handler(func=lambda call: call.data == "boso_gc")
def handle_boso_gc(call):
    user_id = call.from_user.id
    try:
        chat_member = bot.get_chat_member(config.REQUIRED_CHANNEL_ID, user_id)

        if is_user_joined(chat_member):
            bot.answer_callback_query(call.id, "✅ Welcome sa Boso GC!")
        else:
            raise Exception("Not joined")

    except:
        bot.answer_callback_query(call.id, "Opps , please JOIN ✅ first!", show_alert=True)

bot.polling()
