import logging
from time import sleep

import requests
from parsel import Selector

SETTING_USER_AGENT = {"user-agent": "Fake user-agent"}


logger = logging.getLogger(__name__)


def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, headers=SETTING_USER_AGENT, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.ReadTimeout as e:
        logger.error(f"Timeout error: {e}")
        return None


def scrape_novidades(html_content):
    news = []
    selector = Selector(text=html_content)
    for item in selector.css(".entry-preview"):
        url = item.css("a::attr(href)").get()
        news.append(url)
    return news


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    url = "https://blog.betrybe.com/"
    html_content = fetch(url)
    print(scrape_novidades(html_content))
    print(scrape_next_page_link(html_content))
