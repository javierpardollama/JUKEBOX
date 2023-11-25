from models.disk import Disk
import json


class DataService:

    def __init__(self):
        self.data: list[Disk] = []

    def add(self, artist: str, name: str, year: int, gender: str, likes: int):
        self.data.append(Disk(artist, name, year, gender, likes, false))

    def update(self, artist: str, name: str, year: int, gender: str, likes: int):
        idx = map(lambda item: item.name.startswith(
            name), self.data).index(True)
        self.data[idx].artist = artist
        self.data[idx].name = name
        self.data[idx].year = year
        self.data[idx].gender = gender
        self.data[idx].likes = likes

    def delete_by_name(self, name: str):
        self.data.remove(
            next(filter(lambda item: item.name.startswith(name), self.data)))

    def delete_by_artist(self, artist: str):
        list = filter(lambda item: item.artist.startswith(artist), self.data)
        for x in list:
            self.data.remove(x)

    def delete_by_year(self, year: int):
        list = filter(lambda item: item.year == year, self.data)
        for x in list:
            self.data.remove(x)

    def first_by_artist(self, artist: str):
        obj = next(filter(lambda item: item.artist.startswith(artist), self.data))

        return print(obj.__str__())

    def first_by_name(self, name: str):

        obj = next(filter(lambda item: item.name.startswith(name), self.data))

        return print(obj.__str__())

    def first_by_year(self, year: int):

        obj = next(filter(lambda item: item.year == year, self.data))

        return print(obj.__str__())

    def get_all(self):
        list = self.data

        for x in list:
            print(x.__str__())

    def get_all_by_name(self, artist: str):
        list = filter(lambda item: item.name.startswith(artist), self.data)

        for x in list:
            print(x.__str__())

    def get_all_by_artist(self, artist: str):
        list = filter(lambda item: item.artist.startswith(artist), self.data)

        for x in list:
            print(x.__str__())

    def get_all_by_year(self, year: int):
        list = filter(lambda item: item.year == year, self.data)

        for x in list:
            print(x.__str__())

    def get_all_by_gender(self, gender: str):
        list = filter(lambda item: item.gender == gender, self.data)

        for x in list:
            print(x.__str__())

    def load(self):
        with open('./data/data.json') as file:
            temp = json.load(file)
            for x in temp:
                self.data.append(
                    Disk(x['artist'], x['name'], int(x['year']), x['gender'], int(x['likes']), bool(x['bought'])))

    def save(self):
        temp = json.dumps([ob.__dict__ for ob in self.data], indent=4)

        with open("./data/data.json", "w", encoding='utf8') as outfile:
            outfile.write(temp)
