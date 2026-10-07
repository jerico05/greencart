from database.config import get_connection



class StoreRepository:
    connection = get_connection()

    def save_store(self, store):
        cursor = self.connection.cursor()

        sql = """
            INSERT INTO boutique (nom, description, adresse, longitude, latitude, telephone, est_verifie)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql,(store.nom, store.description, store.adress, store.longitude, store.latitude,
                            store.telephone, store.est_verifie))

        return cursor.fetchone()[0]