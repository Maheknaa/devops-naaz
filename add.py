def calculate_bill(units):
    if units <= 100:
        bill = units * 2.60 # 2.60 per unit
    elif units <= 300:
        bill = (100 * 2.60) + (units - 100) * 7.20  # $0.75 per unit for 101-300
    else:
        bill = (100 * 2.60) + (200 * 7.20) + (units - 300) * 9.0 # $1.20 per unit for above 300

    return bill

def main():
    try:
        units = float(input("Enter the number of electricity units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return
        
        bill_amount = calculate_bill(units)
        print(f"Total Electricity Bill: ${bill_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
