class Book:
    def __init__(self, title, author, pages):  # Encapsulation: Constructor to initialize object state
        self._title = title  
        self._author = author 
        self._pages = pages  

    def display_info(self):  # Abstraction: Exposes only necessary features to interact with the class
        print(f"Title: {self._title}")  
        print(f"Author: {self._author}")  
        print(f"Pages: {self._pages}")  


class Fiction(Book):  # Inheritance: Fiction class inherits from Book class
    def __init__(self, title, author, pages, genre): 
        super().__init__(title, author, pages) 
        self._genre = genre  

    def display_genre(self):  # Polymorphism: Method specific to Fiction class
        print(f"Genre: {self._genre}")

    # Polymorphism: Overriding the display_info method
    def display_info(self): 
        super().display_info()  
        self.display_genre()  


class NonFiction(Book):  # Inheritance: NonFiction class inherits from Book class
    def __init__(self, title, author, pages, topic):  
        super().__init__(title, author, pages) 
        self._topic = topic  

    def display_topic(self):  # Polymorphism: Method specific to NonFiction class
        print(f"Topic: {self._topic}")

    # Polymorphism: Overriding the display_info method
    def display_info(self):  
        super().display_info() 
        self.display_topic() 

# Create objects using tuples
fiction_books = [
    ("And Then There Were None", "Agatha Christie", 200, "Mystery"),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 320, "Fantasy")
]
nonfiction_info = ("Sapiens", "Yuval Noah Harari", 443, "History")

# Create objects and call methods
for info in fiction_books:
    fiction_book = Fiction(*info)
    fiction_book.display_info()
    print("-" * 20)
    
nonfiction_book = NonFiction(*nonfiction_info)
nonfiction_book.display_info()
