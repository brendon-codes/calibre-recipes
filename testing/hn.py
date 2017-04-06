#!/usr/bin/env python2

import sys
import json
import requests
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup as BS

ARTICLE_SCORE = 60
ARTICLE_TYPES = frozenset([
    "story"
])
ARTICLE_DOMAINS_EXCLUDE = [
    "nytimes.com",
    "bloomberg.com",
    "economist.com",
    "theatlantic.com",
    "techcrunch.com"
]


def fetch_url(url):
    res = requests.get(url)
    if (res.status_code < 200 or res.status_code > 299):
        return None
    return res.content


def fetch_url_json(url):
    content = fetch_url(url)
    if content is None:
        return None
    obj = json.loads(content)
    return obj


def get_article(article_id):
    base = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
    url = base.format(id=article_id)
    article = fetch_url_json(url)
    return article


def should_skip_art_score(article):
    return (article["score"] < ARTICLE_SCORE)


def should_skip_art_type(article):
    return (article["type"] not in ARTICLE_TYPES)


def should_skip_art_domain(article):
    if "url" not in article:
        return True
    url = article["url"]
    parts = urlparse(url)
    domain = parts.netloc
    for exc_domain in ARTICLE_DOMAINS_EXCLUDE:
        exc_dotdomain = "".join([".", exc_domain])
        if (
                (exc_domain in domain) or 
                (exc_dotdomain in domain)
        ):
            return True
    return False


def should_skip_article(article):
    if should_skip_art_score(article):
        return True
    if should_skip_art_type(article):
        return True
    if should_skip_art_domain(article):
        return True
    return False


def get_comments(article_id):
    base = "https://news.ycombinator.com/item?id={id}"
    url = base.format(id=article_id)
    content = fetch_url(url)
    BS()


def get_articles():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    new_article_ids = fetch_url_json(url)
    if new_article_ids is None:
        return []
    for article_id in new_article_ids:
        article = get_article(article_id)
        if article is None:
            continue
        if should_skip_article(article):
            continue
        print("GO: %s" % article["id"])
    return []


def main():
    get_articles()


if __name__ == "__main__":
    main()
    sys.exit(0)
