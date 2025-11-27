from helpers import calc, string


def main():
    height = 5
    width = 8
    area = calc.area(height, width)
    text = string.shout(f"The area of a {height}-by-{width} rectangle is {area}")
    print(text)


if __name__ == "__main__":
    main()
