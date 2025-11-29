def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats


def main():
    total_players = 0
    while True:
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))

        batting_average = calculate_batting_average(hits, at_bats)

        print(f"Player: {last_name}, Batting Average: {batting_average:.3f}")

        total_players += 1

        continue_program = input("Do you want to enter another player? (Yes/No): ").strip().lower()
        if continue_program != "yes":
            break

    print(f"Total players entered: {total_players}")


main()
