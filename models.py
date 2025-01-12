from configs import db, app
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, )
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    def __init__(self, username, password, role="guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role




login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Artists(db.Model):
    name = db.Column(db.String, nullable=False)
    streams = db.Column(db.String, nullable=False)
    id = db.Column(db.String, primary_key=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        artists = [
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
        for artist_data in artists:
            artist = Artists(id=artist_data["id"], name=artist_data["name"], streams=artist_data["streams"])
            db.session.add(artist)
            db.session.commit()

        admin = User(username='admin', password='admin123', role='admin')
        user = User(username='user', password='123')
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
