from dataclasses import dataclass

@dataclass
class Disk:       
    
    def __init__(self) :        
        pass
    
    def __init__(self, artist:str, name:str, year:int, gender:str) :        
        self.name = name
        self.artist = artist
        self.year = year
        self.gender =gender
        
    
    def __str__(self):
        return f"{self.name}\n{self.artist}\n{self.year}\n{self.gender}"
