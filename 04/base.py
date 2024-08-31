from abc import ABC, abstractmethod
import requests

class Space_news_source(ABC):
    @abstractmethod
    def fetch_news(self):
        pass

    def display_news(self):
        print(self.__class__.__name__)


class NASA_news(Space_news_source):
    def fetch_news(self):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?q=NASA&apiKey=d690b0a4b7b7428993d2c01784326548")
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            formatted_articles = []
            for article in articles:
                title = article.get('title', 'No Title')
                author = article.get('author', 'Unknown Author')
                published_at = article.get('publishedAt', 'Unknown Date')
                source = article.get('source', {}).get('name', 'Unknown Source')
                url = article.get('url', 'No URL')
                formatted_article = f"Title: {title}\nAuthor: {author}\nPublished At: {published_at}\nSource: {source}\nURL: {url}\n"
                formatted_articles.append(formatted_article)
            return "\n".join(formatted_articles)
        else:
            return "Failed to fetch NASA news"
     
class Tesla_news(Space_news_source):
    def fetch_news(self):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?q=tesla&apiKey=d690b0a4b7b7428993d2c01784326548")
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            formatted_articles = []
            for article in articles:
                title = article.get('title', 'No Title')
                author = article.get('author', 'Unknown Author')
                published_at = article.get('publishedAt', 'Unknown Date')
                source = article.get('source', {}).get('name', 'Unknown Source')
                url = article.get('url', 'No URL')
                formatted_article = f"Title: {title}\nAuthor: {author}\nPublished At: {published_at}\nSource: {source}\nURL: {url}\n"
                formatted_articles.append(formatted_article)
            return "\n".join(formatted_articles)
        else:
            return "Failed to fetch Tesla news"
        
class SpaceX_news(Space_news_source):
    def fetch_news(self):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?q=SpaceX&apiKey=d690b0a4b7b7428993d2c01784326548")
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            formatted_articles = []
            for article in articles:
                title = article.get('title', 'No Title')
                author = article.get('author', 'Unknown Author')
                published_at = article.get('publishedAt', 'Unknown Date')
                source = article.get('source', {}).get('name', 'Unknown Source')
                url = article.get('url', 'No URL')
                formatted_article = f"Title: {title}\nAuthor: {author}\nPublished At: {published_at}\nSource: {source}\nURL: {url}\n"
                formatted_articles.append(formatted_article)
            return "\n".join(formatted_articles)
        else:
            return "Failed to fetch SpaceX news"

Nasa = NASA_news()
tesla = Tesla_news()
spacex = SpaceX_news()

news = [Nasa, tesla, spacex]

for n in news:
    print("================================")
    print(n.fetch_news())