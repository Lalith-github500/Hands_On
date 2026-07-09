from abc import ABC, abstractmethod


# Book Entity
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# SRP
class Catalog:
    def add_book(self, book):
        print(f"Added: {book.title}")


# OCP
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, books, keyword):
        pass


class TitleSearch(SearchStrategy):
    def search(self, books, keyword):
        return [b for b in books if keyword.lower() in b.title.lower()]


# ISP
class Searchable(ABC):
    @abstractmethod
    def search(self):
        pass


class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass


# LSP
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


# DIP
class IssueService:
    def __init__(self, notifier: Notification):
        self.notifier = notifier

    def issue_book(self, book):
        print(f"Issuing {book.title}")
        self.notifier.send(f"{book.title} issued")


book = Book("Python Basics", "John Doe")
service = IssueService(EmailNotification())
service.issue_book(book)