class Product:
    def __init__(self, id: int, nom: str, description: str, image: str, prix: float) -> None:
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__image = image
        self.__prix = prix

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_nom(self) -> str:
        return self.__nom

    def set_nom(self, nom: str) -> None:
        self.__nom = nom

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_image(self) -> str:
        return self.__image

    def set_image(self, image: str) -> None:
        self.__image = image

    def get_(self) -> str:
        return self.__unite

    def set_unite(self, unite: str) -> None:
        self.__unite = unite
