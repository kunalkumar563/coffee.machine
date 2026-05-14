# Coffee Machine

A Python project demonstrating object-oriented programming with inheritance. The coffee machine prints ASCII art representations of different coffee types.

## Features

- Abstract base class `Coffee` with inheritance
- Subclasses for different coffee types: Latte, Matcha, Americano, Espresso
- Interactive terminal interface to select and display coffee images
- ASCII art representations using hash symbols

## How to Run

1. Ensure Python 3 is installed
2. Run `python coffee.py`
3. Choose your coffee type from the menu
4. Type 'quit' to exit

## Classes

- `Coffee`: Abstract base class
- `Latte`: Subclass for latte coffee
- `Matcha`: Subclass for matcha coffee
- `Americano`: Subclass for americano coffee
- `Espresso`: Subclass for espresso coffee

Each subclass implements the `print_image()` method to display its unique ASCII art.