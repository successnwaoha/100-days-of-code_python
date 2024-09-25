import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? type the date in this format YYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_website = response.text
# print(billboard_website)

soup = BeautifulSoup(billboard_website, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
    
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="bb471708ac0446e3a1deb36490b1a3d9",
        client_secret="7c3a841c529c40f898cc3fada850f372",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
print(sp)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # print(f"This is the URI: {uri}")
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


# song_titles = soup.find_all(name="h3", id_="title-of-a-story")
# print(song_titles)

#2024-07-12