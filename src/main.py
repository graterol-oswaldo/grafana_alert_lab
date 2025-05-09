import time
from utils import tools
import db


def main():
    count = 0
    switch = False
    while True:
        count += 1
        if tools.is_multiple(count,30):
            switch = not switch

        [low_number, high_number] = [90.0,100.0] if switch else [20.0,30.0]

        rand_number = tools.random_number(low_number, high_number)
        db.insert_data(rand_number)
        time.sleep(1)


if __name__ == "__main__":
    main()
    