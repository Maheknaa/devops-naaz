def reverse_number(number):
    # Check if the number is negative
    negative = False
    if number < 0:
        negative = True
        number = abs(number)
    
    reversed_number = 0
    while number > 0:
        # Extract the last digit
        digit = number % 10
        # Append it to the reversed number
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the number
        number //= 10
    
    # If the original number was negative, make the reversed number negative
    if negative:
        reversed_number = -reversed_number
    
    return reversed_number

def main():
    # Prompt the user to enter a number
    number = int(input("Enter a number: "))
    
    # Reverse the number
    reversed_num = reverse_number(number)
    
    # Print the reversed number
    print(f"The reversed number is: {reversed_num}")

if __name__ == "__main__":
    main()
