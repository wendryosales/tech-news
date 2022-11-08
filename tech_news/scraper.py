import requests
import logging
from time import sleep


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


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
