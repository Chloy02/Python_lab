class Library_item:
    def __init__(self, title , availability = True):
        self.title = title
        self.availability = availability
    
    def get_details(self):
        return f"Title: {self.title}, Availability: {'Available' if self.availability else 'Not Available'}"
    
class Magazine(Library_item):
    def __init__(self, title, issue_number, availability=True):
        super().__init__(title, availability)
        self.issue_number = issue_number

    def get_details(self):
        details = super().get_details()
        return f"{details}, Issue Number: {self.issue_number}"
    
class DVD(Library_item):
    def __init__(self, title, duration, availability=True):
        super().__init__(title, availability)
        self.duration = duration
        
    def get_details(self):
        details = super().get_details()
        return f"{details} Duration: {self.duration}"
    
magazine = Magazine("Times of India", "938236")

dvd = DVD("Tarzen", "25mins")

print(magazine.get_details())
print(dvd.get_details())