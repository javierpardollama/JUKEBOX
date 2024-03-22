from typing import Optional
from services.data_service import DataService


class ShellService:

    exit: bool = False

    def __init__(self) -> None:
        self.data_service = DataService()
        self.data_service.load()

    def main_menu(self) -> None:
        while not self.exit:
            option: str = (input("\n" +
                                 "******* Menu Principal **********  \n" +
                                 "1. Crear Album \n" +
                                 "2. Actualizar Album \n" +
                                 "3. Borrar Albumes > \n" +
                                 "4. Buscar Albumes > \n" +
                                 "5. Salir \n"))

            match option:
                case "1":
                    self.add()
                case "2":
                    self.update()
                case "3":
                    self.delete_menu()
                case "4":
                    self.search_menu()
                case "5":
                    self.stop()
                case other:
                    print("Opcion Incorrecta")

    def delete_menu(self) -> None:
        while not self.exit:
            option: str = input("\n" +
                                "******* Menu de Borrado ********** \n" +
                                "1. Borrar Album por Nombre \n" +
                                "2. Borrar Albumes por Artista \n" +
                                "3. Borrar Albumes por Año \n" +
                                "4. Salir \n")

            match option:
                case "1":
                    self.delete_by_name()
                case "2":
                    self.delete_by_artist()
                case "3":
                    self.delete_by_year()
                case "4":
                    self.main_menu()
                case other:
                    print("Opcion Incorrecta")

    def search_menu(self) -> None:
        while not self.exit:
            option: str = input("\n" +
                                "******* Menu de Búsqueda ********** \n" +
                                "1. Lista Todos los Albumes \n" +
                                "2. Listar Albumes por Nombre \n" +
                                "3. Listar Albumes por Artista \n" +
                                "4. Listar Albumes por Año \n" + +
                                "5. Listar Albumes por Genero \n" +
                                "6. Salir \n")

            match option:
                case "1":
                    self.get_all()
                case "2":
                    self.get_all_by_name()
                case "3":
                    self.get_all_by_artist()
                case "4":
                    self.get_all_by_year()
                case "5":
                    self.get_all_by_gender()
                case "6":
                    self.main_menu()
                case other:
                    print("Opcion Incorrecta")

    def start(self) -> None:
        self.main_menu()

    def stop(self) -> None:
        self.exit = True
        print("Guardando")
        self.data_service.save()
        print("Guardado Completado")
        quit()

    def add(self) -> None:
        artist: str = input("¿Nombre del Artista?")
        name: str = input("¿Nombre del Albumn?")
        year: int = int(input("¿Año de Publicación?"))
        gender: str = input("¿Genero del Albumn?")
        likes: int = Optional[int](input("¿Nº de Likes?"))
        self.data_service.add(artist, name, year, gender, likes)
        print("Disco Creado")

    def update(self) -> None:
        artist: str = input("¿Nombre del Artista?")
        name: str = input("¿Nombre del Albumn?")
        year: int = int(input("¿Año de Publicación?"))
        gender: str = input("¿Genero del Albumn?")
        likes: int = Optional[int](input("¿Nº de Likes?"))
        self.data_service.update(artist, name, year, gender, likes)
        print("Disco Actualizado")

    def delete_by_name(self) -> None:
        name: str = input("¿Nombre del Albumn?")
        self.data_service.delete_by_name(name)
        print("Disco Borrado")

    def delete_by_artist(self) -> None:
        artist: str = input("¿Nombre del Artista?")
        self.data_service.delete_by_artist(artist)
        print("Discos Borrados")

    def delete_by_year(self) -> None:
        year: int = int(input("¿Año de Publicación?"))
        self.data_service.delete_by_year(year)
        print("Discos Borrados")

    def get_all(self) -> None:
        self.data_service.get_all()

    def get_all_by_name(self) -> None:
        name: str = input("¿Nombre del Albumn?")
        self.data_service.get_all_by_name(name)

    def get_all_by_artist(self) -> None:
        artist: str = input("¿Nombre del Artista?")
        self.data_service.get_all_by_artist(artist)

    def get_all_by_year(self) -> None:
        year: int = int(input("¿Año de Publicación?"))
        self.data_service.get_all_by_year(year)

    def get_all_by_gender(self) -> None:
        gender: str = input("¿Genero?")
        self.data_service.get_all_by_gender(gender)


