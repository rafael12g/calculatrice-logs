import socket
import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "127.0.0.1"
PORT = 5000

def lancer_serveur():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((HOST, PORT))
    serveur.listen()

    logging.info("Serveur IoT démarré")
    print("Serveur en attente de connexion...")

    while True:
        conn, addr = serveur.accept()
        with conn:
            logging.info(f"Connexion reçue de {addr}")
            data = conn.recv(1024)

            if data:
                message = data.decode()
                logging.info(f"Donnée reçue : {message}")
                print("Message reçu :", message)

                valeur = float(message.split(":")[1])

                if valeur > 28:
                    logging.warning("ALERTE : Température élevée")


if __name__ == "__main__":
    lancer_serveur()