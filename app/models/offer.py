from datetime import datetime


class Offer:
    def __init__(
        self,
        id: int,
        prix_initial: float,
        prix_reduit: float,
        pourcentage_reduction: float,
        quantite_disponible: int,
        date_debut: datetime,
        date_fin: datetime,
        statut: str,
    ) -> None:
        self.__id = id
        self.__prix_initial = prix_initial
        self.__prix_reduit = prix_reduit
        self.__pourcentage_reduction = pourcentage_reduction
        self.__quantite_disponible = quantite_disponible
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__statut = statut

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_prix_initial(self) -> float:
        return self.__prix_initial

    def set_prix_initial(self, prix_initial: float) -> None:
        self.__prix_initial = prix_initial

    def get_prix_reduit(self) -> float:
        return self.__prix_reduit

    def set_prix_reduit(self, prix_reduit: float) -> None:
        self.__prix_reduit = prix_reduit

    def get_pourcentage_reduction(self) -> float:
        return self.__pourcentage_reduction

    def set_pourcentage_reduction(self, pourcentage_reduction: float) -> None:
        self.__pourcentage_reduction = pourcentage_reduction

    def get_quantite_disponible(self) -> int:
        return self.__quantite_disponible

    def set_quantite_disponible(self, quantite_disponible: int) -> None:
        self.__quantite_disponible = quantite_disponible

    def get_date_debut(self) -> datetime:
        return self.__date_debut

    def set_date_debut(self, date_debut: datetime) -> None:
        self.__date_debut = date_debut

    def get_date_fin(self) -> datetime:
        return self.__date_fin

    def set_date_fin(self, date_fin: datetime) -> None:
        self.__date_fin = date_fin

    def get_statut(self) -> str:
        return self.__statut

    def set_statut(self, statut: str) -> None:
        self.__statut = statut
