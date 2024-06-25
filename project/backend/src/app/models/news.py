from pydantic import BaseModel

class News(BaseModel):
    id: str
    title: str
    content: str