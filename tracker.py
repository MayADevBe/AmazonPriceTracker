import requests
from bs4 import BeautifulSoup
import time
import smtplib
import config

class Tracker:
    """Track Prices and send E-Mail"""
    
    def __init__(self, to_track, recipient):
        self.to_track = to_track
        self.recipient = recipient

    def check(self):    
        for url in self.to_track:
            try:
                source = requests.get(url, headers=config.HEADERS).text
                soup = BeautifulSoup(source, 'lxml')
                # print(soup.prettify())
                title = soup.find('span', id="productTitle").text.strip()
                # print(title)
                price = soup.find('span', id="priceblock_ourprice").text
                price = int(price.split(",")[0])
                # print(price)
                if price <= self.to_track[url]:
                    self.notify(url, title, price)
                    # price drop to wish
                time.sleep(3)
            except:
                time.sleep(3)

    def notify(self, url, title, price):
        try:
            server = smtplib.SMTP(config.SMTPSERVER, config.PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(config.SENDER, config.PASSWORD)
            subject = 'Pricefall!'
            body = f'Price for {title} is now {price}. Check out: {url}'
            msg = f"Subject: {subject}\n\n{body}"
            server.sendmail(config.SENDER, self.recipient, msg)
            print("E-Mail send")
        except Exception as e:
            print(e)
        finally:
            server.quit()

    def add(self, url, price):
        self.to_track[url] = price
    
    def remove(self, url):
        if url in self.to_track.keys:
            del self.to_track[url]