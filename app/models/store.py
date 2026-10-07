class Store:
    def __init__(
        self,
        id: int,
        nom: str,
        description: str,
        adresse: str,
        latitude: float,
        longitude: float,
        telephone: str,
        est_verifie: bool,
    ) -> None:
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__adresse = adresse
        self.__latitude = latitude
        self.__longitude = longitude
        self.__telephone = telephone
        self.__est_verifie = est_verifie

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

    def get_adresse(self) -> str:
        return self.__adresse

    def set_adresse(self, adresse: str) -> None:
        self.__adresse = adresse

    def get_latitude(self) -> float:
        return self.__latitude

    def set_latitude(self, latitude: float) -> None:
        self.__latitude = latitude

    def get_longitude(self) -> float:
        return self.__longitude

    def set_longitude(self, longitude: float) -> None:
        self.__longitude = longitude

    def get_telephone(self) -> str:
        return self.__telephone

    def set_telephone(self, telephone: str) -> None:
        self.__telephone = telephone

    def get_est_verifie(self) -> bool:
        return self.__est_verifie

    def set_est_verifie(self, est_verifie: bool) -> None:
        self.__est_verifie = est_verifie
