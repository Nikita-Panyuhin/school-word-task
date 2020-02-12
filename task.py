# from time import sleep
import os
import matplotlib.pyplot as plt


def main():
    with open("sholohov/_phrases.txt", "r", encoding='utf-8') as file:
        phrases = list(filter(lambda x: x, list(map(lambda x: x.strip(), file.readlines()))))

    count = [0] * len(phrases)
    don = [0] * len(phrases)

    for filename in os.listdir("sholohov"):
        if filename != "_phrases.txt":
            with open("sholohov/" + filename, "r", encoding='utf-8') as file:
                text = file.read().strip()
            if filename == "don.txt":
                for i in range(len(phrases)):
                    if text.count(phrases[i]) != 0:
                        count[i] += (len(text.split()) / len(phrases[i].split())) / text.count(phrases[i])
            else:
                for i in range(len(phrases)):
                    if text.count(phrases[i]) != 0:
                        don[i] += (len(text.split()) / len(phrases[i].split())) / text.count(phrases[i])
            print(filename)

    for i in range(len(count)):
        count[i] = round(count[i] / (len(phrases) - 2), 3)

    print(count)
    print()
    print(don)


if __name__ == "__main__":
    main()
