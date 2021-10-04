import re
import datetime
import telegram
import telebotapi
import pdfplumber
import requests
import telebot
from telegram.ext import *
import Constants as keys
ap_url=''


def start_command(update,context):
    update.message.reply_text('Benvenuto nel TutorBot, creato da Sergio Boffi, per iniziare ad utilizzare il Bot, scrivere "/" ed in seguito il nome della provincia di cui si vuole avere informazioni riguardo ai tutor, ti verranno inviate i nomi delle posizioni dei tutor')
def Abruzzo_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/33/abruzzo.pdf'
    PDF(update, ap_url)
def Basilicata_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/27/basilicata.pdf'
    PDF(update, ap_url)
def Calabria_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/14/calabria.pdf'
    PDF(update, ap_url)
def Campania_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/35/campania.pdf'
    PDF(update, ap_url)
def Emilia_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/13/emilia.pdf'
    PDF(update, ap_url)
def Friuli_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/39/friuli.pdf'
    PDF(update, ap_url)
def Lazio_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/15/lazio.pdf'
    PDF(update, ap_url)
def Liguria_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/31/liguria.pdf'
    PDF(update, ap_url)
def Lombardia_command(update, context):
   ap_url = 'https://www.poliziadistato.it/statics/49/lombardia.pdf'
   PDF(update, ap_url)
def Marche_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/43/marche.pdf'
    PDF(update, ap_url)
def Molise_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/40/molise.pdf'
    PDF(update, ap_url)
def Piemonte_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/46/piemonte.pdf'
    PDF(update, ap_url)
def Puglia_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/40/puglia.pdf'
    PDF(update, ap_url)
def Sardegna_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/41/sardegna.pdf'
    PDF(update, ap_url)
def Sicilia_command(update, context):
    ap_url = "https://www.poliziadistato.it/statics/30/sicilia.pdf"
    PDF(update, ap_url)
def Toscana_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/06/toscana.pdf'
    PDF(update, ap_url)
def Trentino_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/30/trentino.pdf'
    PDF(update, ap_url)
def Umbria_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/24/umbria.pdf'
    PDF(update, ap_url)
def ValleDAosta_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/32/valle_d_aosta.pdf'
    PDF(update, ap_url)
def Veneto_command(update, context):
    ap_url = 'https://www.poliziadistato.it/statics/25/veneto.pdf'
    PDF(update, ap_url)
def PDF(update, ap_url):
    now = datetime.date.today()
    today = now.strftime("%d/%m/%Y")


    def download_file(url):
        local_filename = url.split('/')[-1]

        with requests.get(url) as r:
            with open(local_filename, 'wb') as f:
                f.write(r.content)

        return local_filename
    counter=0
    stampa = False
    ap = download_file(ap_url)
    with pdfplumber.open(ap) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    new_vend_re = re.compile(today)
    for line in text.split('\n'):
        for i in range (6):
            notnow = now + datetime.timedelta(days=i)
            someday = notnow.strftime("%d/%m/%Y")
            if line ==someday:
                stampa = False
        if line == today:
            stampa = True
        if new_vend_re.match(line) or stampa == True:
            update.message.reply_text(line)
            counter=counter+1
    if counter==0:
        update.message.reply_text("Oggi in questa regione non sono presenti tutor accesi")

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
        updater=Updater(keys.API_KEY, use_context=True)
        dp=updater.dispatcher
        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("Lombardia", Lombardia_command))
        dp.add_handler(CommandHandler("ValleDAosta", ValleDAosta_command))
        dp.add_handler(CommandHandler("Piemonte", Piemonte_command))
        dp.add_handler(CommandHandler("Trentino", Trentino_command))
        dp.add_handler(CommandHandler("Veneto", Veneto_command))
        dp.add_handler(CommandHandler("Friuli", Friuli_command))
        dp.add_handler(CommandHandler("Liguria", Liguria_command))
        dp.add_handler(CommandHandler("Emilia", Emilia_command))
        dp.add_handler(CommandHandler("Toscana", Toscana_command))
        dp.add_handler(CommandHandler("Marche", Marche_command))
        dp.add_handler(CommandHandler("Umbria", Umbria_command))
        dp.add_handler(CommandHandler("Sardegna", Sardegna_command))
        dp.add_handler(CommandHandler("Campania", Campania_command))
        dp.add_handler(CommandHandler("Basilicata", Basilicata_command))
        dp.add_handler(CommandHandler("Molise", Molise_command))
        dp.add_handler(CommandHandler("Abruzzo", Abruzzo_command))
        dp.add_handler(CommandHandler("Lazio", Lazio_command))
        dp.add_handler(CommandHandler("Puglia", Puglia_command))
        dp.add_handler(CommandHandler("Sicilia", Sicilia_command))
        dp.add_handler(CommandHandler("Calabria", Calabria_command))
        dp.add_error_handler(error)
        updater.start_polling()
        updater.idle()


main()
