import requests
from bs4 import BeautifulSoup
import telebot
import time

TOKEN = '8706004572:AAEuwJ49X3Z2rvQqm4hPY-qL-BYcjVazWpQ'
CHAT_ID = '386933310'
URL = "https://auctions.yahoo.co.jp/search/search?p=%E3%83%88%E3%83%AA%E3%82%B7%E3%83%86%E3%82%A3&auccat=2084062534&max=50000&price_type=currentcode&s1=new&o1=d"

bot = telebot.TeleBot(TOKEN)
sent_lots = set()

def check():
    try:
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find_all('li', class_='Product')
        for item in items:
            link_tag = item.find('a', class_='Product__titleLink')
            if not link_tag: continue
            href = link_tag.get('href').split('?')[0]
            lot_id = href.split('/')[-1]
            if lot_id not in sent_lots:
                bot.send_message(CHAT_ID, f"🆕 Нашел Tricity!\n{link_tag.text.strip()}\n\n{href}")
                sent_lots.add(lot_id)
    except: pass

if __name__ == '__main__':
    while True:
        check()
        time.sleep(1200)
