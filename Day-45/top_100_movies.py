import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_website = response.text

soup = BeautifulSoup(movies_website, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_list = []

for movie in movies:
    movie_text = movie.getText()
    movies_list.append(movie_text)
    # print(movie_text)
        
with open("movies.txt", "w", encoding="utf-8") as movies_file:
    for movie in reversed(movies_list):
        movies_file.write(movie + '\n')