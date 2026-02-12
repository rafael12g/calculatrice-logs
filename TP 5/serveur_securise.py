import socket
import logging
import time

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "0.0.0.0"
PORT = 6000

# Dictionnaire pour compter les tentatives par IP
tentatives_connexion = {}

SEUIL_TENTATIVES = 5
INTERVALLE = 10  # secondes

def lancer_serveur():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((HOST, PORT))
    serveur.listen()

    print("Serveur sécurisé en écoute...")
    logging.info("Serveur sécurisé démarré")

    while True:
        conn, addr = serveur.accept()
        ip_client = addr[0]
        moment = time.time()

        logging.info(f"Tentative de connexion depuis {ip_client}")

        # Initialisation si nouvelle IP
        if ip_client not in tentatives_connexion:
            tentatives_connexion[ip_client] = []

        # Ajouter la tentative actuelle
        tentatives_connexion[ip_client].append(moment)

        # Supprimer les anciennes tentatives
        tentatives_connexion[ip_client] = [
            t for t in tentatives_connexion[ip_client]
            if moment - t < INTERVALLE
        ]

        #print(f"Nombre de tentatives récentes : {len(tentatives_connexion[ip_client])}")

        # Vérifier dépassement seuil
        if len(tentatives_connexion[ip_client]) >= SEUIL_TENTATIVES:
            logging.warning(f"ALERTE : Trop de connexions depuis {ip_client}")
            print("Alerte intrusion détectée !")

        conn.close()

if __name__ == "__main__":
    lancer_serveur()