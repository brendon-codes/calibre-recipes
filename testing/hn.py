#!/usr/bin/env python2

import sys
import json
import requests
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup as Soup

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
COMMENTS_COUNT = 10


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
    soup = Soup(content)
    com_rows = (
        soup.findAll(
            "tr",
            attrs={
                "class": "athing comtr "
            },
            recursive=True
        )
    )
    comments = []
    for com_row in com_rows:
        comment = parse_comment(com_row)
        if comment is None:
            continue
        comments.append(comment)
    return comments


def parse_comment(com_row):
    if not com_row.has_key("id"):
        return None
    atogg = (
        com_row.find(
            "a",
            attrs={
                "class": "togg"
            }
        )
    )
    if atogg is None:
        return None
    if not atogg.has_key("n"):
        return None
    span_age = (
        com_row.find(
            "span",
            attrs={
                "class": "age"
            }
        )
    )
    if span_age is None:
        return None
    span_age_a = span_age.find("a")
    if span_age_a is None:
        return None
    age = span_age_a.string.strip()
    span_text = (
        com_row.find(
            "span",
            attrs={
                "class": "c00"
            }
        )
    )
    if span_text is None:
        return None
    div_reply = (
        span_text.find(
            "div",
            attrs={
                "class": "reply"
            }
        )
    )
    if div_reply is not None:
        div_reply.extract()
    span_empties = span_text.findAll("span")
    for span_empty in span_empties:
        if (span_empty.string.strip() == ""):
            span_empty.extract()
    text = span_text.renderContents()
    ##
    ## Build output
    ##
    comment = {}
    comment["id"] = int(com_row["id"])
    comment["score"] = int(atogg["n"])
    comment["age"] = age
    comment["text"] = text
    return comment


def filter_comments(all_comments):
    sorted_coms = (
        sorted(
            all_comments,
            key=lambda c: c["score"],
            reverse=True
        )
    )
    comments = sorted_coms[:COMMENTS_COUNT]
    return comments


def process_comments(article_id):
    all_comments = get_comments(article_id)
    comments = filter_comments(all_comments)
    html = format_comments(comments)
    return html


def format_comments(comments):
    out = "<!doctype html>"
    out += "<html lang='en'>"
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

  <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
  <![endif]-->
</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>


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
        comments_html = process_comments(article["id"])
        print(comments_html)
        break
    return []


def main():
    get_articles()


if __name__ == "__main__":
    main()
    sys.exit(0)
