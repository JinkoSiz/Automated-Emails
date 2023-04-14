import requests


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'f7f819cd08994aa6a75f4df622d27d73'

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'
        return url


news_feed = NewsFeed(interest='авто', from_date='2023-02-30', to_date='2023-04-30', language='ru')

print(news_feed.get())
