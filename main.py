
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
    markup.add(types.InlineKeyboardButton("Forward (0/5)", callback_data="forward_check"))
    markup.add(types.InlineKeyboardButton("Join", callback_data="check_join"))

    bot.send_photo(message.chat.id, photo=photo, caption=caption, parse_mode="Markdown", reply_markup=markup)
    photo.close()

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def handle_join_check(call):
    user_id = call.from_user.id
    try:
        chat_member = bot.get_chat_member(config.REQUIRED_CHANNEL_ID, user_id)

        if is_user_joined(chat_member):
            bot.answer_callback_query(call.id, "✅ Already joined!")
        else:
            raise Exception("Not joined")

    except:
        photo = open('media/1234+.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("JOIN ✅", url="https://t.me/+0enGe_F5qDg1ODg1"))
        bot.send_photo(call.message.chat.id, photo=photo, caption="Opps , please JOIN ✅ first!", reply_markup=markup)
        photo.close()

bot.polling()
