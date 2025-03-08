import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters

# Logging einrichten
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Token aus Umgebungsvariable abrufen
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Fehlerbehandlung, falls der Token nicht gefunden wird
if not TELEGRAM_API_TOKEN:
    raise ValueError("❌ Fehler: TELEGRAM_API_TOKEN ist nicht gesetzt. Bitte überprüfe deine Railway-Variables.")

# Start-Befehl
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👋 Hallo! Ich bin deine persönliche KI-Sekretärin.\n"
        "Ich kann dir bei vielen Aufgaben helfen. 😊\n"
        "Was kann ich für dich tun?"
    )

# Beispiel für die Datenerfassung
async def track(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    await update.message.reply_text(f"✅ Verstanden! Ich habe folgendes notiert: {text}")

# Fehlerbehandlung
async def error_handler(update: object, context: CallbackContext) -> None:
    logging.error(f"⚠️ Fehler mit Update {update}: {context.error}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Befehle registrieren
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track))

    # Fehlerbehandlung
    app.add_error_handler(error_handler)

    print("✅ Bot läuft... 🚀")
    app.run_polling()
