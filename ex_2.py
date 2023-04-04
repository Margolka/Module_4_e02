# "Simple calculator operating on two numbers provided by the user"
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def calculator():
    choice = input(
        "Podaj działanie, posługując się odpowiednią liczbą:\n1 Dodawanie\n2 Odejmowanie\n3 Mnożenie\n4 Dzielenie\n"
    )
    if choice in ("1", "2", "3", "4"):
        try:
            a = float(input("Podaj składnik 1 :"))
            b = float(input("Podaj składnik 2 :"))
        except ValueError:
            logging.error("Błędne dane")
            exit(0)
        if choice == "1":
            logging.info("Dodaję %s i %s" % (a, b))
            print("Wynik to", a + b)
        elif choice == "2":
            logging.info("Odejmuję %s od %s" % (b, a))
            print("Wynik to", a - b)
        elif choice == "3":
            logging.info("Mnożę %s i %s" % (a, b))
            print("Wynik to", a * b)
        elif choice == "4":
            if b != 0:
                logging.info("Dzielę %s przez %s" % (a, b))
                print("Wynik to", a / b)
            else:
                logging.error("Nie można dzielić przez 0")
    else:
        logging.error("Błędny wybór!")


if __name__ == "__main__":
    calculator()
