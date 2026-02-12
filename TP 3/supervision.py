import os
import logging
import datetime
import socket

# Configuration du logging
logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def verifier_connectivite(hote):
    logging.info(f"Test de connectivité vers {hote}")

    # -c pour Linux / -n pour Windows
    param = "-n" if os.name == "nt" else "-c"
    commande = f"ping {param} 1 {hote}"

    reponse = os.system(commande)

    if reponse == 0:
        logging.info(f"{hote} est accessible")
        return True
    else:
        logging.warning(f"{hote} ne répond pas")
        return False

def verifier_charge_cpu():
    logging.info("Simulation vérification charge CPU")
    charge = 30  # valeur fictive
    if charge > 80:
        logging.warning("Charge CPU élevée")
    return charge


def verifier_port(hote, port):
    logging.info(f"Test du port {port} sur {hote}")

    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((hote, port))
        logging.info("Port ouvert")
        return True
    except:
        logging.warning("Port fermé ou inaccessible")
        return False
    finally:
        s.close()


if __name__ == "__main__":
    verifier_connectivite("127.0.0.1")  
    verifier_charge_cpu()
    verifier_port("127.0.0.1", 80)