def calculate_salary(hours_worked, hourly_rate):
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5

    return regular_pay + overtime_pay


hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))

salary = calculate_salary(hours, rate)
print(f"Total Salary: ${salary:.2f}")