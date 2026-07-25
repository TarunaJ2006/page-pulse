import pytest
from parser import get_title, count_h1, count_images_missing_alt, count_words
from bs4 import BeautifulSoup


def test_happy_path():
    html = """
    <html>
        <head>
            <title>Example</title>
            <meta name="description" content="Test description">
        </head>
        <body>
            <h1>Main Heading</h1>
            <img src="a.jpg">
            <img src="b.jpg" alt="Image">
            <p>Hello world from Page Pulse.</p>
        </body>
    </html>
    """

    soup = BeautifulSoup(html, "lxml")

    assert get_title(soup) == "Example"
    assert count_h1(soup) == 1
    assert count_images_missing_alt(soup) == 1
    assert count_words(soup) > 0


def test_no_title():
    html = "<html><body><h1>Hello</h1></body></html>"

    soup = BeautifulSoup(html, "lxml")

    assert get_title(soup) == "No title found"


def test_no_images():
    html = "<html><body><h1>Hello</h1></body></html>"

    soup = BeautifulSoup(html, "lxml")

    assert count_images_missing_alt(soup) == 0