import pytest
from book import Book

@pytest.mark.parametrize(('title', 'isbn'),[
    ('To Kill a Mockingbird', '978-0446310789'),
    ('1984', '978 0451524935'),
    ('The Great Gatsby', '9780743273565'),
    ('Moby Dick', '9781503280786'),
    ('War and Peace', '9781400079988'),
    ('Pride and Prejudice', '9781503290563'),
    ('The Catcher in the Rye', '9780316769174'),
    ('The Hobbit', '9780547928227'),
    ('Fahrenheit 451', '9781451673319'),
    ('The Lord of the Rings', '9780544003415'),
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn






@pytest.mark.parametrize(('title', 'isbn'),[
    ('', '9780446310789'),
    (' ', '9780451524935'),
    ('', '9780743273565'),
    ('    ', '9781503280786'),
    ('', '9781400079988'),
    ('', '9781503290563'),
    ('', '9780316769174'),
    (20, '9780547928227'),
    ('        ', '9781451673319'),
    ([''], '9780544003415'),
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)


@pytest.mark.parametrize(('title', 'isbn'),[
    ('To Kill a Mockingbird', '978044631078910000000'),
    ('1984', '9'),
    ('The Great Gatsby', '1111111111111'),
    ('Moby Dick', '0000000000001'),
    ('War and Peace', '9781400079981'),
    ('Pride and Prejudice', '9781503290562'),
    ('The Catcher in the Rye', '9780316769171'),
    ('The Hobbit', '        '),
    ('Fahrenheit 451', ''),
    ('The Lord of the Rings', ' '),
])

def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)