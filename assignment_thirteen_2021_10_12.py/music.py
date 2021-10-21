# 2. Write a simple class to represent a song. there should be just three attributes: 
# title, performer and duration. The class should contain the basic get*, set*, str* and 
# init* methods. Write the main program that will allow user to maintain the collection 
# of songs as a linked structure of doubly linked nodes. The program should have 
# functions for adding a new song, removing a song, modifying the information about 
# existing song, finding and displaying songs with the given author or title.

class Music(object):
    def __init__(self, title: str, performer: str, duration: int) -> None:
        """Initalize a new Music object.

        Args:
            title (str): The title of the song.
            performer (str): The performer who created this song.
            duration (int): The duration of the song in seconds.
        """
        self.title = title
        self.performer = performer
        self.duration = duration

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title    

    def get_performer(self) -> str:
        return self.performer

    def set_performer(self, performer: str) -> None:
        self.performer = performer

    def get_duration(self) -> int:
        return self.duration

    def set_duration(self, duration: int) -> None:
        self.duration = duration

    def __str__(self) -> str:
        return "{a} by {b} - Playtime: {c} seconds.".format(a = self.title, b = self.performer, c = self.duration)
