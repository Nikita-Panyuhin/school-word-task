# from time import sleep
import os
import re
import matplotlib.pyplot as plt


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
                    count[i] += text.count(phrases[i])
        else:
            for i in range(len(phrases)):
                if text.count(phrases[i]) != 0:
                    don[i] += text.count(phrases[i])
        print(filename)

    for i in range(len(phrases)):
        count[i] *= len(phrases[i]) / (texts_length) * 100

    for i in range(len(phrases)):
        don[i] *= len(phrases[i]) / (texts_length) * 100

    delta = [abs(don[i] - count[i]) for i in range(len(phrases))]

    nums = list(range(len(phrases)))
    ans = [y for x, y in sorted(zip(delta, nums), reverse=True)]

    print(count)
    print()
    print(don)

    for e in ans:
        print(phrases[e], delta[e])

    plt.scatter(nums, count, c="#0000ff")
    plt.scatter(nums, don, c="#ff0000")
    plt.scatter(nums, delta, c="#00ff00")
    plt.show()


if __name__ == "__main__":
    main()
