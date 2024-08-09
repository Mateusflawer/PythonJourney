import requests
from bs4 import BeautifulSoup
import re


url = "http://localhost:3000/"
response = requests.get(url)
raw_html = response.content
parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding="utf-8")

select_parser = parsed_html.select_one("#intro > div > div > article > h2")

select_parser_parent = select_parser.parent

if select_parser_parent is not None:
    print(select_parser_parent.text)
