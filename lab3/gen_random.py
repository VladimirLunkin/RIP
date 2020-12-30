from random import randint


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)


def main():
    gen = gen_random(5, 1, 3)
    print(*gen)

    gen = gen_random(5, 1, 3)
    print(*gen)

    gen = gen_random(10, 1, 3)
    print(*gen)


if __name__ == "__main__":
    main()
