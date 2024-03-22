from dataclasses import dataclass
from typing import Optional


@dataclass
class Disk:
    def __init__(self, artist: str, name: str, year: int, gender: str, likes: Optional[int], bought: bool) -> None:
        self.name = name
        self.artist = artist
        self.year = year
        self.gender = gender
        self.likes = likes
        self.bought = bought

    def __str__(self) -> str: 
        return f"{self.name}\n{self.artist}\n{self.year}\n{self.gender}\n{self.likes}\n{self.bought}"
