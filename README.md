# Page Pulse

A lightweight web application that audits any webpage URL and returns useful information about the page through a FastAPI backend and a simple HTML/CSS/JavaScript frontend.

This project was built as part of the **Digital Heroes Software Development (SDE) Training Task**.

## Project Highlights

- Modular backend architecture using FastAPI.
- Clean separation of API, parsing logic, and data models.
- Comprehensive error handling for common failure scenarios.
- Interactive API documentation with Swagger UI.
- Unit-tested parsing logic.

## Features

- Analyze an HTML webpage using its URL.
- Return the HTTP status code.
- Measure the response time.
- Extract the page title.
- Extract the meta description.
- Count H1 headings.
- Count images missing ALT text.
- Estimate the page word count.
- Handle invalid URLs, connection failures, timeouts, HTTP errors, and non-HTML responses with user-friendly messages.
- Interactive API documentation using FastAPI Swagger UI.
- Unit tests for the parsing logic.

## Tech Stack

### Backend
- Python
- FastAPI
- Requests
- BeautifulSoup4
- lxml
- Pydantic

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Testing
- pytest

---

## Project Structure

```
page-pulse/
│
├── backend/
│   ├── main.py
│   ├── parser.py
│   ├── models.py
│   ├── requirements.txt
│   └── tests/
│       └── test_parser.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TarunaJ2006/page-pulse.git
cd page-pulse
```

### 2. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Start the backend server

```bash
python -m uvicorn main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

### 4. Launch the frontend

Open:

```
frontend/index.html
```

in your web browser.

---

## API Contract

### POST `/audit`
Accepts a webpage URL and returns a JSON audit report containing page metadata and basic content statistics.
Analyzes a webpage and returns an audit report.

### Request

```json
{
  "url": "https://example.com"
}
```

### Example Response

```json
{
  "status": 200,
  "response_time_ms": 152.34,
  "title": "Example Domain",
  "meta_description": "No meta description found",
  "h1_count": 1,
  "images_missing_alt": 0,
  "word_count": 21
}
```

### Response Codes

| Status | Description |
|---------|-------------|
| 200 | Audit completed successfully |
| 400 | Invalid URL or unsupported content |
| 408 | Request timed out |
| 503 | Website could not be reached |
| 500 | Unexpected server error |

---

## Running Tests

From the `backend` directory:

```bash
python -m pytest
```

Expected result:

- All tests should pass successfully.

## How to Use

1. Start the FastAPI backend.
2. Open `frontend/index.html` in a modern web browser while the FastAPI backend is running.
3. Enter a valid webpage URL (for example, `https://example.com`).
4. Click **Analyze Website**.
5. Review the generated audit report, which includes:
   - HTTP status
   - Response time
   - Page title
   - Meta description
   - H1 count
   - Images missing ALT text
   - Approximate word count

---

## Design Decisions

### 1. Separated API logic from parsing logic

The project separates the FastAPI application (`main.py`) from the webpage parsing logic (`parser.py`).

**Reason:** This keeps the API layer focused on handling HTTP requests and responses, while the parsing logic remains independent and easier to maintain and test.

---

### 2. Used Pydantic models for request and response validation

The API uses Pydantic models (`models.py`) to define both the request body and the response format.

**Reason:** This provides automatic request validation, generates clear API documentation in Swagger UI, and ensures a consistent response structure.

---

### 3. Added explicit error handling for common failure cases

The application handles invalid URLs, connection failures, request timeouts, HTTP errors, and non-HTML content with descriptive error messages instead of allowing the application to fail unexpectedly.

**Reason:** The assignment specifically emphasizes correctness and error handling. Returning clear messages improves usability and makes the API more robust.

---

## Future Improvements

Given additional development time, the following improvements could be added:

- Cache previously analyzed URLs to reduce repeated network requests.
- Extract additional SEO metrics such as heading hierarchy, broken links, canonical tags, and Open Graph metadata.
- Support asynchronous requests for improved scalability.
- Add Docker support for easier deployment.
- Improve frontend accessibility and responsive design.

---

## Live Demo

### Backend (Render)

Home:
https://page-pulse-21ig.onrender.com/

Swagger UI:
https://page-pulse-21ig.onrender.com/docs

### Frontend (Vercel)

https://page-pulse-taruna2.vercel.app

---

## Submission Notes

This project includes:

- FastAPI backend
- HTML/CSS/JavaScript frontend
- Unit tests for parsing logic
- Interactive API documentation via Swagger UI
- Graceful handling of common error conditions

---

## AI Usage

AI tools were used to brainstorm implementation approaches, understand FastAPI concepts, improve documentation, and troubleshoot deployment issues. The project implementation, code integration, testing, debugging, and final design decisions were completed and verified by me.

---

## Author

Prepared as part of the Digital Heroes Software Development (SDE) Training Task.
