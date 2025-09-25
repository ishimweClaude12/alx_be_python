CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
 


def convert_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return fahrenheit   * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


def main():
    try:
        # Ask user for input
        temp_input = input("Enter the temperature to convert: ").strip()
        
        # Validate numeric input
        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp_value = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
