from threading import Thread
from time import sleep


def cook(name, dish):
    print(f"{name} is washing...")
    sleep(1)
    print(f"{name} is preparing...")
    sleep(1)
    print(f"{name} is cooking {dish}...")
    sleep(1)
    print(f"{name} is serving {dish}...")
    sleep(1)


if __name__ == '__main__':
    t_juan = Thread(target=cook, args=("Juan", "Pique Macho"))
    t_sara = Thread(target=cook, args=("Sara", "Silpancho"))

    t_juan.start()
    t_sara.start()

    t_juan.join()
    t_sara.join()
