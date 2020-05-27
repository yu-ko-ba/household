#!/usr/bin/env python3
import sys
import os
import csv

def main():
    FILE_DIRECTORY = os.path.expanduser('~') + '/Desktop/.household_data.csv'

    with open(FILE_DIRECTORY) as f:
        READER = list(csv.reader(f))[0]
        POCKET_MONEY = int(READER[0])
        CASH = int(READER[1])

        if len(sys.argv) == 1 or sys.argv[1] == "show":
            print("残りの使えるお金は")
            print("おこづかい: " + str(POCKET_MONEY) + "円")
            print("現金      : " + str(CASH) + "円")
            print("です。")
            sys.exit(0)

        if sys.argv[1] == "pocket":
            if sys.argv[2] == "+" or sys.argv[2] == "+=":
                POCKET_MONEY += int(sys.argv[3])
            if sys.argv[2] == "-" or sys.argv[2] == "-=":
                POCKET_MONEY -= int(sys.argv[3])

            if len(sys.argv) > 4:
                if sys.argv[4] == "cash":
                    if sys.argv[5] == "+" or sys.argv[5] == "+=":
                        CASH += int(sys.argv[6])
                    if sys.argv[5] == "-" or sys.argv[5] == "-=":
                        CASH -= int(sys.argv[6])

        if sys.argv[1] == "cash":
            if sys.argv[2] == "+" or sys.argv[2] == "+=":
                CASH += int(sys.argv[3])
            if sys.argv[2] == "-" or sys.argv[2] == "-=":
                CASH -= int(sys.argv[3])

            if len(sys.argv) > 4:
                if sys.argv[4] == "pocket":
                    if sys.argv[5] == "+" or sys.argv[5] == "+=":
                        POCKET_MONEY += int(sys.argv[6])
                    if sys.argv[5] == "-" or sys.argv[5] == "-=":
                        POCKET_MONEY -= int(sys.argv[6])

        with open(FILE_DIRECTORY, 'w') as f:
            WRITER = csv.writer(f)
            WRITER.writerow([POCKET_MONEY, CASH])

        print("残りの使えるお金は")
        print("おこづかい: " + str(POCKET_MONEY) + "円")
        print("現金      : " + str(CASH) + "円")
        print("です。")


if __name__ == '__main__':
    main()
