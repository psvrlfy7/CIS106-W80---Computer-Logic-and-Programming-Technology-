def calculate_mpg_and_gas_cost(miles, gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00  # Assuming $3 per gallon
    return mpg, gas_cost


def main():
    total_miles = 0
    total_gas_cost = 0
    total_trips = 0

    while True:
        destination = input("Enter destination city: ")
        miles = float(input("Enter miles traveled: "))
        gallons = float(input("Enter gallons used: "))

        mpg, gas_cost = calculate_mpg_and_gas_cost(miles, gallons)

        print(f"Destination: {destination}, Miles: {miles}, MPG: {mpg:.2f}, Gas Cost: ${gas_cost:.2f}")

        total_miles += miles
        total_gas_cost += gas_cost
        total_trips += 1

        continue_program = input("Do you want to enter another trip? (Yes/No): ").strip().lower()
        if continue_program != "yes":
            break

    print(f"Total trips: {total_trips}")
    print(f"Total miles traveled: {total_miles}")
    print(f"Total gas cost: ${total_gas_cost:.2f}")


main()
