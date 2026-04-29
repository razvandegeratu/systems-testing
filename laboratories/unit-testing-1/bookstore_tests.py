import pytest

from bookstore.book import Book
from bookstore.book_repository import InMemoryBookRepository
from bookstore.services.book_filtering_service import BookFilterService
from bookstore.services.bookstore_service import BookStoreService


# TODO: Create a fixture that returns a BookService instance
def create_book_service():
    """
    INSTRUCTIONS:
    - Create and return a BookService instance
    - Use InMemoryBookRepository for storage
    - Use default BookFilterService
    
    HINTS:
    repository = ...
    
    book_filter_service = ...
    return BookService(repository, book_filter_service)
    """
    repository = InMemoryBookRepository()
    book_filter_service = BookFilterService()
    return BookStoreService(repository, book_filter_service)


# TODO: Create a fixture that returns a sample book for testing
def create_sample_book():
    """
    INSTRUCTIONS:
    - Create a Book instance with sample data
    - Use realistic values for title, author, genre, and price
    
    REQUIREMENTS:
    - Book should have valid, testable attributes
    """

    book = Book(title = "Garry Potter", author = "JK Rowling", genre = "Fantasy", price = 15.99)
    return book


# INFO: For the following tests, use only the BookService instance created by the fixture
def test_add_book():
    """
    TESTING OBJECTIVES:
    1. Create a book service using the fixture
    2. Create a sample book using the fixture
    3. Add the book to the service
    4. Verify:
       - Book has a non-None ID
       - Book attributes match the original book
    
    HINTS:
    - Use assertions to check book details
    - Verify ID is automatically assigned
    """
    # Your implementation here
    book = create_sample_book()
    book_service = create_book_service()
    book_service.add_book(book)
    assert book.id is not None
    assert book.title == "Garry Potter"
    assert book.author == "JK Rowling"
    assert book.genre == "Fantasy"
    assert book.price == 15.99


def test_add_book_validation():
    """
    TESTING OBJECTIVES:
    1. Attempt to add a book with invalid data
    2. Verify appropriate exception is raised
    
    REQUIREMENTS:
    - Test scenarios like:
      * Book with empty title
      * Book with empty author
     de cen
    HINTS:
    - Use pytest.raises() to check for exceptions
    """
    book_service = create_book_service()
    book1 = Book(title = "", author = "JK Rowling", genre = "Fantasy", price = 15.99)
    book2 = Book(title = "Garry Potter", author = "", genre = "Fantasy", price = 15.99)
    
    with pytest.raises(ValueError): 
        book_service.add_book(book1)
    with pytest.raises(ValueError):
        book_service.add_book(book2)

    


# INFO: Here you should use @pytest.mark.parametrize to test multiple genres
def test_get_books_by_genre():
    """
    TESTING OBJECTIVES:
    1. Add multiple books with different genres
    2. Filter books by specific genres
    3. Verify:
       - Only books of the specified genre are returned
       - Filtering is case-insensitive
    
    REQUIREMENTS:
    - Add books across multiple genres
    - Test filtering with different genre inputs
    
    HINTS:
    - Use service's get_books() method with genre parameter
    - Check length and genre of returned books
    """

    book1 = Book(title = "Hunger Games", author = "Suzanne Collins", genre = "Dystopian", price = 15.99)
    book2 = Book(title = "Harry Potter", author = "JK Rowling", genre = "Fantasy", price = 15.99)
    book3 = Book(title = "Hamlet", author = "William Shakespeare", genre = "Classic", price = 15.99)
    book_service = create_book_service()
    book_service.add_book(book1)
    book_service.add_book(book2)
    book_service.add_book(book3)
    fantasy_books = book_service.get_books(genre="Fantasy")
    assert len(fantasy_books) == 1
    assert fantasy_books[0].genre == "Fantasy"
    assert fantasy_books[0].title == "Harry Potter"
    dystopian_books = book_service.get_books(genre="Dystopian")
    assert len(dystopian_books) == 1
    assert dystopian_books[0].genre == "Dystopian"
    assert dystopian_books[0].title == "Hunger Games"
    classic_books = book_service.get_books(genre="Classic")
    assert len(classic_books) == 1
    assert classic_books[0].genre == "Classic"
    assert classic_books[0].title == "Hamlet"
    


# INFO: Here you should use @pytest.mark.parametrize to test multiple price ranges
def test_price_range_filtering():
    """
    TESTING OBJECTIVES:
    1. Add books at different price points
    2. Test filtering by:
       - Minimum price
       - Maximum price
       - Combined price range
    
    REQUIREMENTS:
    - Verify correct number of books returned
    - Ensure only books within price range are included
    
    HINTS:
    - Add books with varied prices
    - Use get_books() with min_price and max_price
    - Test edge cases and different price combinations
    """
    # Your implementation here
    book1 = Book(title = "Book A", author = "Author A", genre = "Genre A", price = 10.00)
    book2 = Book(title = "Book B", author = "Author B", genre = "Genre B", price = 20.00)
    book3 = Book(title = "Book C", author = "Author C", genre = "Genre C", price = 30.00)
    book_service = create_book_service()
    book_service.add_book(book1)
    book_service.add_book(book2)
    book_service.add_book(book3)
    books_min_price = book_service.get_books(min_price=15.00)
    assert len(books_min_price) == 2
    assert all(book.price >= 15.00 for book in books_min_price)
    books_max_price = book_service.get_books(max_price=25.00)
    assert len(books_max_price) == 2
    assert all(book.price <= 25.00 for book in books_max_price)
    books_price_range = book_service.get_books(min_price=15.00, max_price=25.00)
    assert len(books_price_range) == 1
    assert books_price_range[0].price == 20.00



def test_update_book():
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Update the book's details
    3. Verify:
       - Specific attributes can be updated
       - Updated values are correct
       - Other attributes remain unchanged
    
    REQUIREMENTS:
    - Test updating multiple attributes
    - Ensure update works for different book properties
    
    HINTS:
    - Use update_book() method
    - Compare book before and after update
    """
    # Your implementation here
    book = create_sample_book()
    book_service = create_book_service()
    book_service.add_book(book)
    book_service.update_book(book.id, title="Harry Potter and the Sorcerer's Stone", price=12.99)
    updated_book = book_service.get_book_by_id(book.id)
    assert updated_book.title == "Harry Potter and the Sorcerer's Stone"
    assert updated_book.price == 12.99


def test_remove_book():
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Remove the book
    3. Verify:
       - Book is successfully removed
       - Attempting to retrieve the book returns None
    
    REQUIREMENTS:
    - Test successful book removal
    - Test removing a non-existent book
    
    HINTS:
    - Use remove_book() method
    - Check return value of remove operation
    - Verify book is no longer in the service
    """
    # Your implementation here

    book = create_sample_book()
    book_service = create_book_service()
    book_service.add_book(book)
    removed_book = book_service.remove_book(book.id)
    assert removed_book is not None
    assert removed_book is True
    assert book_service.get_book_by_id(book.id) is None

