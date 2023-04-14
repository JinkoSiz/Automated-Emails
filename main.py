import time

import yagmail
import pandas
from news import NewsFeed
import datetime


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language='ru')
    email = yagmail.SMTP(user='gmail', password='password')
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\nSee what's on about {row['interest']} today. {news_feed.get()}")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 43:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
