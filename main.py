from tokenize_text import tokenize_text
from petition_url import url_user
from article_name import name_file_user
from convertgTTS_to_MP3 import convert_to_MP3
from newspaper import Article

tokenize_text()

url = url_user()

article_name = name_file_user()

article = Article(url)

article.download()
article.parse()

content = article.text

convert_to_MP3(content, article_name)

