import requests


def test_has_form():
    response = requests.get("http://localhost:8000/books/new")
    assert "title" in response.text
    assert "author" in response.text
    assert "year" in response.text
    assert "total_pages" in response.text
    assert "genre" in response.text


def test_validate_empty_form():
    data = {"title": ""}
    response = requests.post("http://localhost:8000/books/new", data=data)
    assert response.status_code == 422


def test_post():
    data = {
        "title": "Абай",
        "author": "Мухтар Ауэзов",
        "year": 1942,
        "total_pages": 512,
        "genre": "Роман",
    }

    response = requests.post(
        "http://localhost:8000/books/new", data=data, allow_redirects=False
    )
    assert response.status_code == 303


def test_get_books_1():
    response = requests.get("http://localhost:8000/books/1")
    assert "To Kill a Mockingbird" in response.text
    assert "Harper Lee" in response.text
    assert "1960" in response.text
    assert "336" in response.text
    assert "Fiction" in response.text


def test_get_books():
    response = requests.get("http://localhost:8000/books")
    assert "To Kill a Mockingbird" in response.text
    assert "Harper Lee" in response.text
    assert "1960" in response.text
    assert "336" in response.text
    assert "Fiction" in response.text
    assert "1984" in response.text
    assert "George Orwell" in response.text
    assert "1949" in response.text
    assert "328" in response.text
    assert "Dystopian" in response.text
    assert "The Great Gatsby" in response.text
    assert "F. Scott Fitzgerald" in response.text
    assert "1925" in response.text
    assert "180" in response.text
    assert "Classic" in response.text
    assert "The Lord of the Rings" in response.text
    assert "J.R.R. Tolkien" in response.text
    assert "1954" in response.text
    assert "1178" in response.text
    assert "Fantasy" in response.text
    assert "The Catcher in the Rye" in response.text
    assert "J.D. Salinger" in response.text
    assert "1951" in response.text
    assert "224" in response.text
    assert "Coming-of-age" in response.text
    assert "Абай" in response.text
    assert "Мухтар Ауэзов" in response.text
    assert "1942" in response.text
    assert "512" in response.text
    assert "Роман" in response.text
