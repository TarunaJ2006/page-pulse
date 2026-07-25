from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

from models import URLRequest, AuditResponse
from parser import audit_page

app = FastAPI(
    title="Page Pulse API",
    description="Analyze any webpage and return useful information.",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://page-pulse-tau-five.vercel.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to Page Pulse API"}


@app.post("/audit", response_model=AuditResponse)
def audit(request: URLRequest):

    try:
        report = audit_page(request.url)
        return report

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except requests.exceptions.MissingSchema:
        raise HTTPException(
            status_code=400,
            detail="Invalid URL. Please include http:// or https://"
        )

    except requests.exceptions.InvalidURL:
        raise HTTPException(
            status_code=400,
            detail="Invalid URL."
        )

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=408,
            detail="Request timed out."
        )


    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to the website."
        )
    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Website returned HTTP {e.response.status_code}."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )