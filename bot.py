import time
import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace with your actual token
TOKEN = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"

def start(update: Update, context: CallbackContext):
    user_full_name = update.effective_user.full_name
    bot_name = context.bot.first_name

    # Send initial message
    message = update.message.reply_text("Processing...")

    # React with 🔥 after 2 seconds
    time.sleep(2)
    context.bot.send_message(chat_id=update.effective_chat.id, text="🔥")

    # Send sticker after 2 seconds
    time.sleep(2)
    sticker_message = context.bot.send_sticker(chat_id=update.effective_chat.id,
                                                sticker="CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA")

    # Delete sticker after 2 seconds
    time.sleep(2)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sticker_message.message_id)

    # Send ▣☐☐ after 2 seconds
    message = context.bot.send_message(chat_id=update.effective_chat.id, text="▣☐☐")

    # Edit message with ☐▣☐ after 2 seconds
    time.sleep(2)
    context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                   message_id=message.message_id,
                                   text="☐▣☐")

    # Edit message with ☐☐▣ after 2 seconds
    time.sleep(2)
    context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                   message_id=message.message_id,
                                   text="☐☐▣")

    # Send photo with buttons after 2 seconds
    time.sleep(2)
    keyboard = [
        [InlineKeyboardButton("✇ Aɴɪᴍᴇ Gʀᴏᴜᴘ ✇", url="https://t.me/Cartoon_Heaven")],
        [InlineKeyboardButton("❁ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ❁", url="https://t.me/Cartoon_Carnival")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo="https://te.legra.ph/file/d05ac856c4a8659de29ce.jpg",
                           caption=f"Hᴇʟʟᴏ {user_full_name}✨ Mʏsᴇʟғ {bot_name} Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ? I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!",
                           reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
