from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(source.text,'html.parser')

movies = soup.find('tbody',class_="lister-list").find('tr')
print(movies)
# print(len(movies))
name = movies.find('td',class_="titleColumn").a.text
print(name)
rankAndYear = movies.find('td',class_="titleColumn").get_text(strip=True).split('.')
# print(rankAndYear)
rank = rankAndYear[0]
# print(rank)
year = movies.find('td',class_="titleColumn").span.text.strip('()')
# print(year)
rating = movies.find('td',class_="ratingColumn imdbRating").strong.text
# print(rating)
print(rank,name,year,rating)