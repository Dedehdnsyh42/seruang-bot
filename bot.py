from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Masukkan API Token dari BotFather
TOKEN = "7354641871:AAG7FzK0Ei5a3BV6sP8SdvNjT7yoCyz-ung"

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Halo! Saya adalah bot Telegram.")

# Konfigurasi bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah
    app.add_handler(CommandHandler("start", start))

    # Menjalankan bot
    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
from telegram.ext import MessageHandler, Filters

# Fungsi untuk auto-reply
def reply_text(update: Update, context: CallbackContext):
    user_message = update.message.text
    update.message.reply_text(f"Kamu berkata: {user_message}")

# Tambahkan handler pesan ke bot
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_text))
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Fungsi untuk menampilkan tombol
def menu(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Website", url="https://example.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Pilih opsi:", reply_markup=reply_markup)

# Tambahkan handler untuk tombol
dp.add_handler(CommandHandler("menu", menu))
