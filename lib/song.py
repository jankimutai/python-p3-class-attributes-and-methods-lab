class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name, artist,genre):
        self.name=name
        self.artist = artist
        self.genre = genre
        Song.count +=1
        self.genres.append(genre)
        self.artists.append(artist)

        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    def add_to_artists(cls,artist):
        cls.artists.append(artist)
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    def add_to_artist_count(cls,artist):
        if artist in cls.genre_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


