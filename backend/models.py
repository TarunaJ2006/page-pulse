from pydantic import BaseModel


class URLRequest(BaseModel):
    url: str


class AuditResponse(BaseModel):
    status: int
    response_time_ms: float
    title: str
    meta_description: str
    h1_count: int
    images_missing_alt: int
    word_count: int