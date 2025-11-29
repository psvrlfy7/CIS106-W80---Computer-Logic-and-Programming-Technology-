def calculate_pay_rate_and_gross(job_code, hours_worked):
    if job_code == "L":
        pay_rate = 25.00
    elif job_code == "A":
        pay_rate = 30.00
    elif job_code == "J":
        pay_rate = 50.00
    else:
        pay_rate = 0.00

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        gross_pay = hours_worked * pay_rate

    return pay_rate, gross_pay


def main():
    total_gross_pay = 0
    while True:
        last_name = input("Enter employee's last name: ")
        job_code = input("Enter employee's job code (L, A, or J): ").strip().upper()
        hours_worked = float(input("Enter hours worked: "))

        pay_rate, gross_pay = calculate_pay_rate_and_gross(job_code, hours_worked)

        print(
            f"Employee: {last_name}, Hours Worked: {hours_worked}, Pay Rate: ${pay_rate:.2f}, Gross Pay: ${gross_pay:.2f}")

        total_gross_pay += gross_pay

        continue_program = input("Do you want to enter another employee? (Yes/No): ").strip().lower()
        if continue_program != "yes":
            break

    print(f"Total gross pay: ${total_gross_pay:.2f}")


main()

