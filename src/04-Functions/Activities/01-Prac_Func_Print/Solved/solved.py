def convert_minutes_to_hours(minutes):
    # Convert minutes to hours.
    hours = minutes/60
    # Return the time duration in hours.
    return hours

if __name__ == "__main__":
    # Prompt the user to enter the time duration in minutes.
    amt_minutes = float(input("Enter the time duration in minutes: "))
    # Call the function and store the result in a variable.
    minutes_converted = convert_minutes_to_hours(amt_minutes)
    # Print the time duration in hours.
    print(f"{amt_minutes:.2f} minutes is equal to {minutes_converted:.2f} hours.")