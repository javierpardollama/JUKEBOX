from dataclasses import dataclass


@dataclass
class Disk:
    def __init__(self, artist: str, name: str, year: int, gender: str, likes: int, bought: bool):
        self.name = name
        self.artist = artist
        self.year = year
        self.gender = gender
        self.likes = likes
        self.bought = bought

    def __str__(self):
        return f"{self.name}\n{self.artist}\n{self.year}\n{self.gender}\n{self.likes}\n{self.bought}"
