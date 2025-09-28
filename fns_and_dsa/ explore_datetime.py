from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculates and displays a future date.

    Args:
        current_date (datetime): The starting date.
        days_to_add (int): The number of days to add.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """
    Main function to run the datetime operations.
    """
    current_date = display_current_datetime()
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()