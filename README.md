# Coffee Machine

A Coffee Machine project built using Python and Object-Oriented Programming (OOP). This application allows users to choose from a menu of drinks, process payments, and make coffee while managing resources and tracking profits.

## Features:
- **Interactive User Interface**: Choose a drink from the menu.
- **Resource Management**: Tracks water, milk, and coffee ingredients.
- **Payment System**: Accepts coin payments and processes transactions.
- **Profit Tracking**: Keeps track of the money received and the current profit.
- **Reports**: Allows users to view machine status and profit.

## Files:
- **coffee_machine.py**: Contains the `CoffeeMaker` class responsible for managing resources and making coffee.
- **main.py**: The main program controlling the flow of operations.
- **menu.py**: Models the coffee menu with available drinks and their ingredients.
- **money_machine.py**: Handles coin payment processing and tracks profit.

## Requirements:
- Python 3.8 or greater
- No external libraries required (uses built-in Python libraries).

## Installation:
1. Clone or download the repository.
2. Ensure Python >= 3.8 is installed on your system.
3. Run the `main.py` file in your preferred Python environment (e.g., IDLE, PyCharm, or the terminal).

## How to Use:
1. Run the program.
2. Choose a drink from the available options by typing the drink's name.
3. Insert coins as prompted.
4. The machine will deduct the ingredients and prepare the coffee if resources are sufficient and payment is complete.
5. Type `report` to check machine status or `exit` to stop the program.
