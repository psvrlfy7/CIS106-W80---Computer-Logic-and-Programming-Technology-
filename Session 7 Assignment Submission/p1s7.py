def calculate_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total -= total * 0.10
    return total


def main():
    total_extended_price = 0
    while True:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        total = calculate_total(quantity, price)

        print(f"Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")

        total_extended_price += total

        continue_program = input("Do you want to enter another item? (Yes/No): ").strip().lower()
        if continue_program != "yes":
            break

    print(f"Total extended price: ${total_extended_price:.2f}")


main()
