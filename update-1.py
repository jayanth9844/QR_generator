#telegram bot to convert text to Qrcode
#author:JAYANTH RAJ G
#date:01-02-2024


#import modules
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext,ApplicationBuilder
import qrcode
import io
import os
from dotenv import load_dotenv


#to load environment module
load_dotenv()
API=os.getenv("TOKEN")


#define function
async def start(update:Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome 🙏 to QR_generator\nPlease Enter the text/URL to convert to QR_code.")#replay the text after /start command

async def create_img(update:Update, context: CallbackContext):
    text:str=update.message.text #to store replay text in text variable
    img=qrcode.make(text) #to make qr code and store in img variable
    with io.BytesIO() as img_file: #to create buffer memory
        img.save(img_file,"PNG") #save image in pgn file format
        img_file.seek(0) #point the reading pointer to starting point of the img_file
        await context.bot.send_photo(chat_id=update.effective_chat.id,photo=img_file) #sending photo of QR


# Create and run the bot
application = ApplicationBuilder().token(API).build()
application.add_handler(CommandHandler("start",start))
application.add_handler(MessageHandler(filters.TEXT, create_img))
application.run_polling()
