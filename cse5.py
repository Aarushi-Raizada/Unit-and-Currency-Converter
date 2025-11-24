import sys
import os
from datetime import datetime

# --- Mock Exchange Rates for Currency Conversion ---
# NOTE: Using hardcoded rates. Replace with API calls for live data.
MOCK_EXCHANGE_RATES = {
    'USD': {'EUR': 0.93, 'GBP': 0.81, 'JPY': 150.00, 'INR': 83.00, 'USD': 1.0},
    'EUR': {'USD': 1.08, 'GBP': 0.87, 'JPY': 161.00, 'INR': 89.00, 'EUR': 1.0},
    'GBP': {'USD': 1.23, 'EUR': 1.15, 'JPY': 185.00, 'INR': 102.00, 'GBP': 1.0},
    'JPY': {'USD': 0.0067, 'EUR': 0.0062, 'GBP': 0.0054, 'INR': 0.55, 'JPY': 1.0},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0098, 'JPY': 1.82, 'INR': 1.0}
}

# --- Unit Conversion Factors ---
UNIT_FACTORS = {
    'LENGTH': {
        ('meter', 'feet'): 3.28084,
        ('feet', 'meter'): 1 / 3.28084,
        ('km', 'mile'): 0.621371,
        ('mile', 'km'): 1 / 0.621371,
    },
    'MASS': {
        ('kg', 'pound'): 2.20462,
        ('pound', 'kg'): 1 / 2.20462,
    },
}

# --- History Manager Class ---
class HistoryManager:
    """Manages saving and viewing conversion history in data/history.txt."""
    
    def __init__(self, directory="data", filename="history.txt"):
        self.directory = directory
        self.filepath = os.path.join(self.directory, filename)
        # Ensure the 'data' directory exists
        os.makedirs(self.directory, exist_ok=True)

    def save_history(self, record):
        """Appends a conversion record to the history file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_record = f"[{timestamp}] {record}"
        
        try:
            with open(self.filepath, "a") as f:
                f.write(full_record + "\n")
        except IOError:
            print(f"Error: Could not write to history file at {self.filepath}")

    def view_history(self):
        """Reads and prints the entire conversion history."""
        print("\n--- Conversion History ---")
        try:
            with open(self.filepath, "r") as f:
                data = f.read()
                if not data.strip():
                    print("No history found.")
                else:
                    print(data)
        except FileNotFoundError:
            print("History file not found or no history recorded yet.")
            
# --- Conversion Functions ---

def convert_currency(history_manager):
    """
    Handles user input for currency conversion and saves history.
    """
    try:
        from_currency = input("Enter currency to convert FROM (e.g., USD, EUR): ").upper()
        to_currency = input("Enter currency to convert TO (e.g., USD, EUR): ").upper()
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("\n❌ Invalid input. Please enter a numerical amount.")
        return

    if from_currency not in MOCK_EXCHANGE_RATES or to_currency not in MOCK_EXCHANGE_RATES:
        print(f"Error: Currency not supported. Supported: {', '.join(MOCK_EXCHANGE_RATES.keys())}")
        return

    rate = MOCK_EXCHANGE_RATES[from_currency].get(to_currency)

    if rate is None:
        print(f"Error: Conversion rate from {from_currency} to {to_currency} not available.")
        return

    converted_amount = amount * rate
    
    result_str = f"{amount:.2f} {from_currency} = {converted_amount:.4f} {to_currency} (Rate: {rate:.4f})"
    print(f"\n✅ Result: {result_str}")
    history_manager.save_history(f"[CURRENCY] {result_str}")


def _convert_temperature(value, from_unit, to_unit):
    """Internal function for temperature conversion logic."""
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    
    if from_unit == to_unit: return value

    # Convert to a base unit (Kelvin) first
    if from_unit == 'C': k_value = value + 273.15
    elif from_unit == 'F': k_value = (value - 32) * (5/9) + 273.15
    elif from_unit == 'K': k_value = value
    else: return f"Error: Unsupported temperature unit '{from_unit}'. Use C, F, or K."

    # Convert from Kelvin to the target unit
    if to_unit == 'C': return k_value - 273.15
    elif to_unit == 'F': return (k_value - 273.15) * (9/5) + 32
    elif to_unit == 'K': return k_value
    else: return f"Error: Unsupported temperature unit '{to_unit}'. Use C, F, or K."

def convert_unit(history_manager):
    """
    Handles user input for general unit conversion and saves history.
    """
    try:
        unit_type = input("Enter Unit Type (e.g., LENGTH, MASS, TEMPERATURE): ").upper()
        value = float(input("Enter value to convert: "))
        from_unit = input("Enter unit to convert FROM (e.g., meter, kg, C): ").lower()
        to_unit = input("Enter unit to convert TO (e.g., feet, pound, F): ").lower()
    except ValueError:
        print("\n❌ Invalid input. Please enter a numerical value.")
        return
    except Exception as e:
        print(f"\n❌ An error occurred during input: {e}")
        return

    if unit_type == 'TEMPERATURE':
        result = _convert_temperature(value, from_unit, to_unit)
    
    elif unit_type in UNIT_FACTORS:
        factor = UNIT_FACTORS[unit_type].get((from_unit, to_unit))
        if factor is not None:
            result = value * factor
        elif from_unit == to_unit:
            result = value
        else:
            result = f"Error: Conversion from {from_unit} to {to_unit} in category {unit_type} not defined."
    else:
        result = f"Error: Unit type '{unit_type}' not supported. Supported: {', '.join(UNIT_FACTORS.keys())}, TEMPERATURE"

    if isinstance(result, str) and result.startswith("Error"):
        print(f"\n❌ {result}")
    else:
        result_str = f"{value:.4f} {from_unit.upper()} = {result:.4f} {to_unit.upper()}"
        print(f"\n✅ Result: {result_str}")
        history_manager.save_history(f"[{unit_type}] {result_str}")


# --- Main Application Loop ---
def main():
    """Main function to run the interactive converter with history."""
    
    # Initialize the history manager
    history = HistoryManager()

    while True:
        print("\n===== UNIT & CURRENCY CONVERTER =====")
        print("1. Unit Converter (Length, Mass, Temp)")
        print("2. Currency Converter (USD, EUR, etc.)")
        print("3. View Conversion History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            convert_unit(history)

        elif choice == "2":
            convert_currency(history)

        elif choice == "3":
            history.view_history()

        elif choice == "4":
            print("Thank you for using the converter! 👋")
            sys.exit(0)

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()