from abc import abstractmethod, ABC

class NewsFetchError(Exception):
    def __init__(self, message, url = None, status_code = None):
        super().__init__(message)
        self.url = url
        self.status_code = status_code

    def __str__(self):
        error_message = f"{self.__class__.__name__}: {self.args[0]}"
        if self.url:
            error_message += f"\n URL: {self.url}"
        if self.status_code:
            error_message += f"\n Status Code: {self.status_code}"
        return error_message

class DataAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        pass 

    def displayData(self):
        print(self.__class__.__name__)

class SpaceNewsDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        nasa_count = data.lower().count("nasa")
        spacex_count = data.lower().count("spacex")
        mission_count = data.lower().count("mission")
        
        print("Space News Data Analysis:")
        print(f"Mentions of NASA: {nasa_count}")
        print(f"Mentions of SpaceX: {spacex_count}")
        print(f"Mentions of missions: {mission_count}")

    def displayData(self):
        print("Space News Data Analysis:")
        super().displayData()


class FinancialNewsDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        stock_count = data.lower().count("stock")
        market_count = data.lower().count("market")
        earnings_count = data.lower().count("earnings")
        
        print("Financial News Data Analysis:")
        print(f"Mentions of stock: {stock_count}")
        print(f"Mentions of market: {market_count}")
        print(f"Mentions of earnings: {earnings_count}")

    def displayData(self):
        print("Financial News Data Analysis:")
        super().displayData()


def analyze_data(analyzer: DataAnalyzer, data):
    try:
        analyzer.analyze(data)
        analyzer.displayData()
    except Exception as e:
        print(f"An error occurred: {e}")

space_news_analyzer = SpaceNewsDataAnalyzer()
financial_news_analyzer = FinancialNewsDataAnalyzer()

space_news_data = "NASA launches new space telescope for a mission to Mars."
financial_news_data = "Stock market hits record high after Tesla's earnings report."

# Analyze the data
analyze_data(space_news_analyzer, space_news_data)
analyze_data(financial_news_analyzer, financial_news_data)
