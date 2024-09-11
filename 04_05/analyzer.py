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

