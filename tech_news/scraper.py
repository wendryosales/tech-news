import logging
from time import sleep

import requests
from parsel import Selector

from tech_news.database import create_news

SETTING_USER_AGENT = {"user-agent": "Fake user-agent"}


logger = logging.getLogger(__name__)


def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, headers=SETTING_USER_AGENT, timeout=3)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout) as e:
        logger.error(f"Error: {e}")
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


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author > a::text").get()
    comments_count = selector.css("a.comments-link::text").get()
    comments_count = comments_count if comments_count else 0
    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    tags = selector.css("a[rel=tag]::text").getall()
    category = selector.css(".category-style > span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


def get_tech_news(amount):
    all_news = []
    last_news = []
    url = "https://blog.betrybe.com/"
    while len(all_news) < amount:
        news = scrape_novidades(fetch(url))
        all_news.extend(news)
        next_page_link = scrape_next_page_link(fetch(url))
        url = next_page_link

    for url_new in all_news[:amount]:
        last_news.append(scrape_noticia(fetch(url_new)))
    create_news(last_news)
    return last_news
