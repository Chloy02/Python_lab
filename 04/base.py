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
        api_key = "d690b0a4b7b7428993d2c01784326548"
        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
        if response.status_code == 200:
            return response.json().get('title', 'No Title') + ":" + response.json().get('explanation', 'No Details')
        else:
            return "Failed to fetch NASA news"
        
