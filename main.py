from list import Node
from list import List


def main():
    lst = List()
    lst.append(10)
    lst.append(20)

    [print(item) for item in lst]


if __name__ == '__main__':
    main()
