class Song:
    """class to represent a song

    Attributes:
        tittle (str): Tittle of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'tittle' attribute
            artist (Artist): At artist object representing the song's creator.
            duration (Operational[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
        """

        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album released.
        Artist: (Artist): The artist responsible for the album. If not specified, the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methos:
        addSong: Used to add a new son to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song):A song to add.
            position (Optional[int]): If specified, the song will be added to that position in the track list - inserting in between other songs if necessary. Otherwise, the song will be added to the end of the list.
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by this artists.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
            add_album: use to add a new album to the artist's album llist
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a album to the list.

        Args:
            album (Album): Album object to add to the list.
            If the album is already present, it will not added again.


        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
