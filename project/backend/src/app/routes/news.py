from fastapi import APIRouter
from database.repository.news import NewsDAO
from app.models.news import News

router = APIRouter()

@router.get("/all")
def all():
    DAO = NewsDAO()
    response = DAO.get_all()
    return response

@router.post("/create")
def create(new_news: News):
    DAO = NewsDAO()
    response = DAO.create(new_news)
    return response

@router.post("/update")
def update(news: News):
    DAO = NewsDAO()
    response = DAO.update(news)
    return response

@router.post("/delete/{id}")
def delete(id: str):
    DAO = NewsDAO()
    response = DAO.delete(id)
    return response