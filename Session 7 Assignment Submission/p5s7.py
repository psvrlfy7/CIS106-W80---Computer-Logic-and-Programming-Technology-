def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        tuition = credit_hours * 250.00
    elif district_code == "O":
        tuition = credit_hours * 550.00
    else:
        tuition = 0.00

    return tuition


def main():
    total_tuition = 0
    while True:
        last_name = input("Enter student's last name: ")
        credit_hours = int(input("Enter credit hours: "))
        district_code = input("Enter district code (I for in-district, O for out-of-district): ").strip().upper()

        tuition = calculate_tuition(credit_hours, district_code)

        print(f"Student: {last_name}, Tuition Owed: ${tuition:.2f}")

        total_tuition += tuition

        continue_program = input("Do you want to enter another student? (Yes/No): ").strip().lower()
        if continue_program != "yes":
            break

    print(f"Total tuition owed: ${total_tuition:.2f}")


main()
