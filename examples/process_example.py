import multiprocessing as mp
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
    p_juan = mp.Process(target=cook, args=("Juan", "Pique Macho"))
    p_sara = mp.Process(target=cook, args=("Sara", "Silpancho"))

    p_juan.start()
    p_sara.start()

    p_juan.join()
    p_sara.join()
