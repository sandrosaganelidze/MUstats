from flask import render_template, request, redirect
from forms import *
import requests
from configs import *
from models import *
from flask_login import current_user, login_user, logout_user




@app.route('/')
def index():
    return render_template('about.html')

artists_list = [
    {"name": "Taylor Swift", "streams": "26.6 billion streams", "id": "06HL4z0CvFAxyc27GXpf02"},
    {"name": "The Weeknd", "streams": "20.4 billion streams", "id": "1Xyo4u8uXC1ZmMpatF05PJ"},
    {"name": "Bad Bunny", "streams": "18.9 billion streams", "id": "4q3ewBCX7sLwd24euuV69X"},
    {"name": "Drake", "streams": "17.8 billion streams", "id": "3TVXtAsR1Inumwj472S9r4"},
    {"name": "Billie Eilish", "streams": "15.2 billion streams", "id": "6qqNVTkY8uBg9cP3Jd7DAH"},
    {"name": "Karol G", "streams": "13.7 billion streams", "id": "790FomKkXshlbRYZFtlgla"},
    {"name": "Morgan Wallen", "streams": "13.1 billion streams", "id": "3oDbviiivRWhXwIE8hxkVV"},
    {"name": "SZA", "streams": "12.5 billion streams", "id": "7tYKF4w9nC0nq9CsPZTHyP"},
    {"name": "Ed Sheeran", "streams": "12.2 billion streams", "id": "6eUKZXaKkcviH0Ku9w2n3V"},
    {"name": "Ariana Grande", "streams": "11.8 billion streams", "id": "66CXWjxzNUsdJxJ2JdwvnR"},
    {"name": "Peso Pluma", "streams": "11.6 billion streams", "id": "2xK6qcvIMYUyjqHf4llQ1E"},
    {"name": "Sabrina Carpenter", "streams": "10.9 billion streams", "id": "74KM79TiuVKeVCqs8QtB0B"},
    {"name": "Post Malone", "streams": "10.7 billion streams", "id": "246dkjvS1zLTtiykXe5h60"},
    {"name": "Kendrick Lamar", "streams": "10.4 billion streams", "id": "2YZyLoL8N0Wb9xBt1NhZWg"},
    {"name": "Olivia Rodrigo", "streams": "10.3 billion streams", "id": "1McMsnEElThX1knmY4oliG"},
    {"name": "Doja Cat", "streams": "9.9 billion streams", "id": "5cj0lLjcoR7YOSnhnX0Po5"},
    {"name": "Tyler, The Creator", "streams": "9.7 billion streams", "id": "4V8LLVI7PbaPR0K2TGSxFF"},
    {"name": "J Balvin", "streams": "9.3 billion streams", "id": "1vyhD5VmyZ7KMfW5gqLgo5"},
    {"name": "Harry Styles", "streams": "9.1 billion streams", "id": "6KImCVD70vtIoJWnq6nGn3"},
    {"name": "Beyoncé", "streams": "8.9 billion streams", "id": "6vWDO969PvNqNYHIOW5v0m"},
    {"name": "Zach Bryan", "streams": "8.7 billion streams", "id": "4MNq0sBKT6hW3a1P8A1nqx"},
    {"name": "Rosalía", "streams": "8.4 billion streams", "id": "7ltDVBr6mKbRvohxheJ9h1"},
    {"name": "Travis Scott", "streams": "8.1 billion streams", "id": "0Y5tJX1MQlPlqiwlOH1tJY"},
    {"name": "Anitta", "streams": "7.8 billion streams", "id": "45eNHdiiAbvmbp4erw26rg"},
    {"name": "Lil Baby", "streams": "7.5 billion streams", "id": "5f7VJjfbwm532GiveGC0ZK"},
    {"name": "Marshmello", "streams": "7.3 billion streams", "id": "64KEffDW9EtZ1y2vBYgq8T"},
    {"name": "Dua Lipa", "streams": "7.1 billion streams", "id": "6M2wZ9GZgrQXHCFfjv46we"},
    {"name": "Kanye West", "streams": "7.0 billion streams", "id": "5K4W6rqBFWDnAN6FQUkS6x"},
    {"name": "Shakira", "streams": "6.8 billion streams", "id": "0EmeFodog0BfCgMzAIvKQp"},
    {"name": "Lil Uzi Vert", "streams": "6.7 billion streams", "id": "4O15NlyKLIASxsJ0PrXPfz"},
    {"name": "Nicki Minaj", "streams": "6.5 billion streams", "id": "0hCNtLu0JehylgoiP8L4Gh"},
    {"name": "Chris Stapleton", "streams": "6.3 billion streams", "id": "4YLQaW1UU3mrVetC8gNklR"},
    {"name": "Coldplay", "streams": "6.1 billion streams", "id": "4gzpq5DPGxSnKTe4SA8HAU"},
    {"name": "BLACKPINK", "streams": "6.0 billion streams", "id": "41MozSoPIsD1dJM0CLPjZF"},
    {"name": "Lana Del Rey", "streams": "5.8 billion streams", "id": "00FQb4jTyendYWaN8pK0wa"},
    {"name": "Metro Boomin", "streams": "5.6 billion streams", "id": "0iEtIxbK0KxaSlF7G42ZOp"},
    {"name": "Imagine Dragons", "streams": "5.4 billion streams", "id": "53XhwfbYqKCa1cC15pYq2q"},
    {"name": "Halsey", "streams": "5.3 billion streams", "id": "26VFTg2z8YR0cCuwLzESi2"},
    {"name": "Maluma", "streams": "5.1 billion streams", "id": "1bAftSH8umNcGZ0uyV7LMg"},
    {"name": "Justin Bieber", "streams": "5.0 billion streams", "id": "1uNFoZAHBGtllmzznpCI3s"},
    {"name": "Lil Nas X", "streams": "4.9 billion streams", "id": "7jVv8c5Fj3E9VhNjxT4snq"},
    {"name": "Future", "streams": "4.8 billion streams", "id": "1RyvyyTE3xzB2ZywiAwp0i"},
    {"name": "Camila Cabello", "streams": "4.6 billion streams", "id": "4nDoRrQiYLoBzwC5BhVJzF"},
    {"name": "Bad Omens", "streams": "4.5 billion streams", "id": "3nFkdlSjzX9mRTtwJOzDYB"},
    {"name": "Meghan Trainor", "streams": "4.3 billion streams", "id": "6JL8zeS1NmiOftqZTRgdTz"},
    {"name": "Adele", "streams": "4.2 billion streams", "id": "4dpARuHxo51G3z768sgnrY"},
    {"name": "Sam Smith", "streams": "4.1 billion streams", "id": "2wY79sveU1sp5g7SokKOiI"},
    {"name": "Tame Impala", "streams": "4.0 billion streams", "id": "5INjqkS1o8h1imAzPqGZBb"},
]

@app.route('/artists', methods=['GET', 'POST'])
def artistlist():

    return render_template('artists.html', artists=artists_list)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect("/artists")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET), data=data)
    print(response.json()["access_token"])
    return response.json()["access_token"]


@app.route("/artist/<artist_id>")
def artist_page(artist_id):
    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}

    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    albums_response = requests.get(albums_url, headers=headers)
    albums_data = albums_response.json()["items"]
    albums = albums_data[:8]

    top_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"
    top_tracks_response = requests.get(top_tracks_url, headers=headers)
    top_tracks_data = top_tracks_response.json()["tracks"]
    top_tracks = top_tracks_data[:5]

    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    artist_response = requests.get(artist_url, headers=headers)
    artist_data = artist_response.json()
    artist_name = artist_data["name"]
    artist_img = artist_data["images"][0]["url"]

    return render_template("artist.html", albums=albums, tracks=top_tracks, name=artist_name, img=artist_img)


@app.route("/album_register", methods=["GET", "POST"])
def album_register():
    form = AlbumRegisterForm()
    if request.method == "POST":
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template('album_register.html', form=form)


@app.route("/album_login", methods=["GET", "POST"])
def album_login():
    form = AlbumloginForm()
    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect("/artists")
    return render_template('album_login.html', form=form)


@app.route("/album/<album_id>")
def get_album_tracks(album_id):
    token = get_spotify_token()
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    album_url = f"https://api.spotify.com/v1/albums/{album_id}"
    album_response = requests.get(album_url, headers=headers)
    album_data = album_response.json()["images"]
    album_name = album_response.json()["name"]

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []

    tracks_data = response.json()["items"]
    tracks = [{"name": track["name"], "id": track["id"],
               "artists": ", ".join([artist["name"] for artist in track["artists"]])} for track in tracks_data]
    return render_template("album.html", tracks=tracks, album=album_data, album_name=album_name)
