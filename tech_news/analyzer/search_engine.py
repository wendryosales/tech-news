from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)
    return [(item["title"], item["url"]) for item in response]


def search_by_date(date):
    try:
        formated_data = datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": formated_data.strftime("%d/%m/%Y")}}
    except ValueError:
        raise ValueError("Data inválida.")
    response = search_news(query)
    return [(item["title"], item["url"]) for item in response]


def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    response = search_news(query)
    return [(item["title"], item["url"]) for item in response]


def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    response = search_news(query)
    return [(item["title"], item["url"]) for item in response]
