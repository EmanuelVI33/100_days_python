from os import system

bidders = {}


def add_new_bidder(name, bid: int) -> None:
    bidders[name] = bid


def winner():
    may = 0
    name_may = ""
    for name in bidders:
        if bidders[name] > may:
            may = bidders[name]
            name_may = name
    print(f"{name_may}  {bidders[name_may]}")


def main():
    new_bidder = True
    while new_bidder:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        add_new_bidder(name, bid)
        another_bidder = input("Are there any other bidders? Type 'Yes' or 'No'")
        if another_bidder.lower() == "no":
            new_bidder = False
            winner()
        elif another_bidder.lower() == "yes":
            system("clear")


if __name__ == '__main__':
    main()
    print(bidders)


