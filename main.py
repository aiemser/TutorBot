import re

import datetime
import pdfplumber
import requests
from telegram.ext import *
import Constants as keys

def start_command(update,context):
    update.message.reply_text('Benvenuto nel TutorBot, creato da Sergio Boffi, per iniziare ad utilizzare il Bot, scrivere "/" ed in seguito il nome della provincia di cui si vuole avere informazioni riguardo ai tutor, ti verranno inviate i nomi delle posizioni dei tutor')
def Lombardia_command(update, context):
    now = datetime.date.today()
    today = now.strftime("%d/%m/%Y")
    notnow = now + datetime.timedelta(days=1)
    tomorrow = notnow.strftime("%d/%m/%Y")
    def download_file(url):
        local_filename = url.split('/')[-1]

        with requests.get(url) as r:
            with open(local_filename, 'wb') as f:
                f.write(r.content)

        return local_filename
    stampa=False
    ap_url = 'https://www.poliziadistato.it/statics/39/lombardia.pdf'
    ap = download_file(ap_url)
    with pdfplumber.open(ap) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    new_vend_re = re.compile(today)
    for line in text.split('\n'):
        if line == tomorrow:
            stampa=False
        if line==today:
            stampa=True
        if new_vend_re.match(line)or stampa==True:
            update.message.reply_text(line)


def bossetti_command(update, context):
        update.message.reply_text('GODOOOOO')


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
        updater=Updater(keys.API_KEY, use_context=True)
        dp=updater.dispatcher
        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("Lombardia", Lombardia_command))
        dp.add_handler(CommandHandler("bossetti", bossetti_command))
        dp.add_error_handler(error)
        updater.start_polling()
        updater.idle()


main()








