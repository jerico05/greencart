from datetime import datetime
from decimal import Decimal


class Reservation:
    def __init__(
        self,
        id: int,
        quantite: int,
        montant_total: float,
        code_reservation: str,
        statut: str,
        date_reservation: datetime,
    ) -> None:
        self.__id = id
        self.__quantite = quantite
        self.__montant_total = montant_total
        self.__code_reservation = code_reservation
        self.__statut = statut
        self.__date_reservation = date_reservation

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_quantite(self) -> int:
        return self.__quantite

    def set_quantite(self, quantite: int) -> None:
        self.__quantite = quantite

    def get_montant_total(self) -> float:
        return self.__montant_total

    def set_montant_total(self, montant_total: float) -> None:
        self.__montant_total = montant_total

    def get_code_reservation(self) -> str:
        return self.__code_reservation

    def set_code_reservation(self, code_reservation: str) -> None:
        self.__code_reservation = code_reservation

    def get_statut(self) -> str:
        return self.__statut

    def set_statut(self, statut: str) -> None:
        self.__statut = statut

    def get_date_reservation(self) -> datetime:
        return self.__date_reservation

    def set_date_reservation(self, date_reservation: datetime) -> None:
        self.__date_reservation = date_reservation
