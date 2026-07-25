import requests
import time
from bs4 import BeautifulSoup
def get_title(soup):
    """Extract the page title."""
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "No title found"
def get_meta_description(soup):
    """Extract the meta description."""
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        return meta["content"].strip()
    return "No meta description found"
def count_h1(soup):
    """Count all H1 tags."""
    return len(soup.find_all("h1"))
def count_images_missing_alt(soup):
    """Count images without alt text."""
    images = soup.find_all("img")
    missing_alt = 0

    for image in images:
        alt = image.get("alt")
        if alt is None or alt.strip() == "":
            missing_alt += 1

    return missing_alt
def count_words(soup):
    """Count approximate visible words."""
    text = soup.get_text(separator=" ", strip=True)
    words = text.split()
    return len(words)
def audit_page(url):
    """
    Fetch a webpage and return an audit report.
    """

    start_time = time.time()

    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    response.raise_for_status()
    
    
    response_time = round((time.time() - start_time) * 1000, 2)
    content_type = response.headers.get("Content-Type", "").lower()
    if "text/html" not in content_type:
        raise ValueError(
            f"Unsupported content type: {content_type}. Please provide an HTML webpage."
    )

    content_type = response.headers.get("Content-Type", "")

    if "text/html" not in content_type:
        raise ValueError("The URL does not point to an HTML page.")

    soup = BeautifulSoup(response.text, "lxml")

    report = {
        "status": response.status_code,
        "response_time_ms": response_time,
        "title": get_title(soup),
        "meta_description": get_meta_description(soup),
        "h1_count": count_h1(soup),
        "images_missing_alt": count_images_missing_alt(soup),
        "word_count": count_words(soup)
    }

    return report