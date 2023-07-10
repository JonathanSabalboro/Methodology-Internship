# -*- coding: utf-8 -*-

from requests_html import HTMLSession
import re
import pandas as pd

url_base = 'https://news.google.com/rss/search?q='

s = HTMLSession()


data = []
queries = ["South America", "Argentina",
           "Bolivia", "Brazil", "Chile",
           "Colombia", "Ecuador", "Guyana"
           "Paraguay", "Peru", "Suriname",
           "Uruguay", "Venezuela"]

for query in queries:
    url = url_base + query
    r = s.get(url)
    for title in r.html.find('title'):
        cleaned_title = re.sub(r"[^\w\s]", "", title.text)
        data.append({"Title": cleaned_title, "Query": query})

df = pd.DataFrame(data)
df.to_csv("titles_data.csv", index=False)
