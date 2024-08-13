from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = 'Token yang lo dapetin setelah setup di botfather'
BOT_USERNAME: Final = 'nama bot lo yang lo setup di botfather'

#Command Awal Ketika pertama kali interaksi
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, terimakasih telah mengirimkan pesan! saya adalah ex_mangoding bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, inilah adalah help command')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, ini adalah custom command')

#Bot Response berdasarkan keyword/Command yang di input pengguna telegram
def handle_response(text: str):
    processed: str = text.lower()


    if 'halo' in processed:
        return "Halo, selamat datang di bot exmangoding"
    if 'order' in processed:
        return "Silakan Copy Paste format dibawah ini \n\n <pre><b>Saya ingin Order</b> Nama: \n Email: \n nomor telepon: \n Alamat:</pre>"
    if 'follow' in processed:
        return 'thanks bro'
    
    return 'mon maap saya nggak paham maksud kamu'

#Function untuk handle message, pengecekan message datang dari chat pribadi/grup
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')


    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)
    

        
    print('Bot : ', response)
    await update.message.reply_text(response,parse_mode='HTML')


#Function untuk cek error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update : {update} caused error {context.error}')


#RUN The Code
if __name__ == '__main__':
    print('starting bot....')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Pools the bot 
    print('Polling....')
    app.run_polling(poll_interval=3)