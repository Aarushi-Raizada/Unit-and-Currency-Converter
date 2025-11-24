# Unit-and-Currency-Converter
## Unit and Currency Converter

This is a Python-based command-line utility for performing currency and unit conversions, featuring persistent history tracking for all conversions.

## Features

Currency Conversion: Convert amounts between major currencies (USD, EUR, GBP, JPY, INR) using mock, hardcoded rates.

Unit Conversion: Convert between common units in categories:

Length: Meter <--> Feet, Kilometers <--> Miles.

Mass: Kilograms <--> Pounds.

Temperature: Conversions between Celsius ($C$), Fahrenheit ($F$), and Kelvin ($K$).

Persistent History: All successful conversions are logged with a timestamp to a file (data/history.txt) and can be viewed anytime within the application.

## Requirements

This application requires Python 3.x. No external libraries are strictly necessary as it uses standard built-in modules (sys, os, datetime).

## Installation and Setup

Clone the Repository

Save the Script:
Ensure the provided Python code is saved as converter.py (or any name you choose) in the root directory.

Usage

Run the script directly from your terminal:

python converter.py


The application will present an interactive menu:

===== UNIT & CURRENCY CONVERTER =====
1. Unit Converter (Length, Mass, Temp)
2. Currency Converter (USD, EUR, etc.)
3. View Conversion History
4. Exit
Enter your choice: 


1. Unit Conversion Example

Select 1.

Enter Unit Type: LENGTH

Enter value to convert: 100

Enter unit to convert FROM: meter

Enter unit to convert TO: feet

Output:

✅ Result: 100.0000 METER = 328.0840 FEET


2. Currency Conversion Example

Select 2.

Enter currency to convert FROM: USD

Enter currency to convert TO: JPY

Enter amount to convert: 500

Output:

✅ Result: 500.00 USD = 75000.0000 JPY (Rate: 150.0000)


3. History

Conversion history is stored in the file data/history.txt. The HistoryManager class automatically creates the data directory if it does not exist.

To view the history, select option 3 from the main menu.

Notes on Data

Mock Rates: The currency exchange rates (MOCK_EXCHANGE_RATES) are hardcoded and intended for demonstration. For production use, they should be replaced with calls to a live Exchange Rate API.

Temperature Logic: Temperature conversions are implemented via an internal function that utilizes Kelvin as the intermediate base unit for reliable conversion between Celsius, Fahrenheit, and Kelvin.
