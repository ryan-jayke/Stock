import requests
from bs4 import BeautifulSoup as bs
import time
import smtplib
from email.mime.text import MIMEText as email
import subprocess

def StockAlert(Item, URL, phrase, sender, receiver, pw):
    subprocess.Popen('caffeinate')                              # prevent sleep
    stock = 0                                                   # initiate stock variable
    while stock != -1:                                          # initiate loop, continue until in stock
        page = requests.get(URL)                                # obtain URL
        pagetext = bs(page.text.upper(), 'html.parser')         # convert URL to uppercase text
        stock = pagetext.text.find(phrase.upper())              # search URL for 'out of stock', update stock variable to character position, -1 = not found
        print(Item, ': ', time.ctime(time.time()), ' ', stock)  # print attempt: time & stock variable

        if stock == -1:                                         # if 'out of stock' not found (-1), then email alert and end loop
            print(Item, ' in stock!')
            msg = email(Item + """ in stock!

""" + URL)
            msg['Subject'] = 'Stock Alert: ' + Item
            msg['From'] = sender
            msg['To'] = receiver

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(sender, pw)
            print('login success')
            server.sendmail(sender, receiver, msg.as_string())
            print('message sent')
            server.quit()
            break

        a = 1                                                   # if not in stock, wait for 1 hour, print 'Running' confirmation every 10 minutes
        while a <= 6:
            time.sleep(600)
            print('Running ', time.ctime(time.time()))
            a = a + 1

StockAlert(
    Item = input('Item: '),
    URL = input('URL: '),
    phrase = input('Out of Stock phrase: '),
    sender = input('Sender Email: '),
    receiver = input('Receiver Email: '),
    pw = input('Email password: ')
)