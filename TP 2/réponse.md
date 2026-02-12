# réponse code

```py
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Programme démarré")
logging.warning("Calcul en cours")
logging.error("Erreur : valeur incorrecte")
```
## exo 2
```
INFO
INFO
ERROR
```


## TP 1

```py
import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Programme démarré")

def addition(a, b):
    return a + b

logging.info("additions effectuées")

def division(a, b):
    if b == 0:
        return None
    return a / b

logging.info("divisions effectuées")

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
print("Résultat de l'addition :", resultat_addition)

resultat_division = division(x, y)
if resultat_division is not None:
    print("Résultat de la division :", resultat_division)
else:
    print("Division impossible")
    logging.error("division impossible")


logging.info("calculs effectués")
```


