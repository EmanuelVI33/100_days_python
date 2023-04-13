import os
import random


def chosen_card() -> int:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def show_cards(player_c, total: int, computer_c: int) -> None:
    print(f"Your card {player_c}, current score: {total}")
    print(f"Computer first card: {computer_c}")


def blackjack():
    player_cards = []
    computer_cards = []
    os.system("cls")
    print("Game Blackjack 🂷 🂦")

    for _ in range(2):
        player_cards.append(chosen_card())
        computer_cards.append(chosen_card())

    player_total_card = sum(player_cards)
    computer_total_card = sum(computer_cards)
    is_game_over = False
    while not is_game_over:
        show_cards(player_cards, player_total_card, computer_cards[0])
        if player_total_card > 21 or computer_total_card == 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                card = chosen_card()
                player_cards.append(card)
                player_total_card += card
                if 11 in player_cards and player_total_card > 21:
                    player_cards.remove(11)
                    player_cards.append(1)
                    player_total_card -= 10
            else:
                is_game_over = True

    while computer_total_card < 17:
        card = chosen_card()
        computer_cards.append(card)
        computer_total_card += card

    print(f"Your final hand: {player_cards}, final score: {player_total_card}")
    print(f"Computer's final hand: {computer_cards}, score: {computer_total_card}")
    if player_total_card > 21 and computer_total_card > 21:
        print("You went over. You lose 😤")

    if player_total_card == computer_total_card:
        print("Draw 🙃")
    elif computer_total_card == 21 and computer_cards.__len__() == 2:
        print("Lose, opponent has Blackjack 😱")
    elif player_total_card == 21 and player_cards.__len__() == 2:
        print("Win with a Blackjack 😎")
    elif player_total_card > 21:
        print("You went over. You lose 😭")
    elif computer_total_card > 21:
        print("Opponent went over. You win 😁")
    elif player_total_card > computer_total_card:
        print("You win 😃")
    else:
        print("You lose 😤")


def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()
    print("Bye :3")


if __name__ == '__main__':
    main()

