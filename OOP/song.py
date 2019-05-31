class Song:
    """class to represent a song

    Attributes:
        tittle (str): Tittle of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, tittle, artist, duration=0):
        """Song init method

        Args:
            tittle (str): Initialises the 'tittle' attribute
            artist (Artist): At artist object representing the song's creator.
            duration (Operational[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
        """

        self.tittle = tittle
        self.artist = artist
        self.duration = duration


# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        album_name (str): The name of the album.
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

