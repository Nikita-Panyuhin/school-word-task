# from time import sleep
import os
import re
import matplotlib.pyplot as plt


def find(phrase, text):
    return text.count(phrase)


def main():
    with open("sholohov/_phrases.txt", "r", encoding='utf-8') as file:
        phrases = list(filter(lambda x: x, list(map(lambda x: x.strip().lower(), file.readlines()))))

    texts_length = 0
    count = [0] * len(phrases)
    don = [0] * len(phrases)

    for filename in os.listdir("sholohov"):
        if filename == "_phrases.txt":
            continue

        with open("sholohov/" + filename, "r", encoding='utf-8') as file:
            text = file.read().strip().lower()

        texts_length += len(text.split())

        if filename == "don.txt":
            for i in range(len(phrases)):
                if text.count(phrases[i]) != 0:
                    count[i] += find(phrases[i], text)
        else:
            for i in range(len(phrases)):
                if text.count(phrases[i]) != 0:
                    don[i] += find(phrases[i], text)
        print(filename)

    for i in range(len(phrases)):
        count[i] *= len(phrases[i]) * 100000 / (texts_length)

    for i in range(len(phrases)):
        don[i] *= len(phrases[i]) * 100000 / (texts_length)

    delta = [abs(don[i] - count[i]) for i in range(len(phrases))]

    print()
    print(count)
    print()
    print(don)
    print()

    def f(o):
        return [y for x, y in sorted(zip(delta, o))]
    count = f(count)
    don = f(don)
    phrases = f(phrases)

    nums = list(range(len(phrases)))
    ans = [y for x, y in sorted(zip(delta, nums), reverse=True)]
    delta.sort()

    for e in ans:
        print(phrases[e], delta[e])

    SMALL_SIZE = 6

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=8)     # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=SMALL_SIZE)   # fontsize of the figure title

    plt.xticks(rotation=-90)

    plt.scatter(phrases, count, c="#0000ff").set_label('All')
    plt.scatter(phrases, don, c="#ff0000").set_label('Don')
    plt.scatter(phrases, delta, c="#00ff00").set_label('Delta')
    plt.show()


if __name__ == "__main__":
    main()
